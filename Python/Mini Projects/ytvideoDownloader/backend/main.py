"""
YouTube Video Downloader — FastAPI Backend
Provides REST API endpoints for fetching video info and downloading videos.
"""

import os
import uuid
import glob
import asyncio
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, field_validator

import yt_dlp

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------

app = FastAPI(
    title="YouTube Video Downloader API",
    description="Backend API for the YouTube Video Downloader web application",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DOWNLOAD_DIR = os.path.join(os.path.dirname(__file__), "downloads")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Request / Response models
# ---------------------------------------------------------------------------

class VideoUrlRequest(BaseModel):
    url: str

    @field_validator("url")
    @classmethod
    def validate_url(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("URL cannot be empty")
        # Basic check — yt-dlp will do full validation
        if "youtube.com" not in v and "youtu.be" not in v:
            raise ValueError("Please provide a valid YouTube URL")
        return v


class DownloadRequest(BaseModel):
    url: str
    format_id: Optional[str] = "best"


class FormatInfo(BaseModel):
    format_id: str
    ext: str
    resolution: str
    type: str  # "Combined", "Video Only", "Audio Only"
    vcodec: str
    acodec: str
    filesize: Optional[int] = None
    note: str


class VideoInfoResponse(BaseModel):
    title: str
    thumbnail: str
    duration: int  # seconds
    duration_string: str
    channel: str
    view_count: Optional[int] = None
    upload_date: Optional[str] = None
    formats: list[FormatInfo]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _classify_format(vcodec: str, acodec: str) -> str:
    has_video = vcodec and vcodec != "none"
    has_audio = acodec and acodec != "none"
    if has_video and has_audio:
        return "Combined"
    elif has_video:
        return "Video Only"
    elif has_audio:
        return "Audio Only"
    return "N/A"


def _format_duration(seconds: int) -> str:
    h, remainder = divmod(seconds, 3600)
    m, s = divmod(remainder, 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def _cleanup_old_files():
    """Remove download files older than 10 minutes."""
    import time
    now = time.time()
    for f in glob.glob(os.path.join(DOWNLOAD_DIR, "*")):
        if os.path.isfile(f) and now - os.path.getmtime(f) > 600:
            try:
                os.remove(f)
            except OSError:
                pass


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get("/api/health")
async def health():
    return {"status": "ok", "service": "yt-downloader-api"}


@app.post("/api/video-info", response_model=VideoInfoResponse)
async def video_info(req: VideoUrlRequest):
    """Fetch video metadata and available download formats."""
    _cleanup_old_files()

    ydl_opts = {"quiet": True, "no_warnings": True}

    try:
        loop = asyncio.get_event_loop()
        info = await loop.run_in_executor(None, _extract_info, req.url, ydl_opts)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to fetch video info: {str(e)}")

    raw_formats = info.get("formats", [])
    formats: list[FormatInfo] = []

    for f in raw_formats:
        vcodec = f.get("vcodec") or "none"
        acodec = f.get("acodec") or "none"
        ftype = _classify_format(vcodec, acodec)

        if ftype == "N/A":
            continue

        formats.append(FormatInfo(
            format_id=str(f.get("format_id", "")),
            ext=f.get("ext", ""),
            resolution=f.get("resolution") or f.get("format_note", "N/A"),
            type=ftype,
            vcodec=vcodec[:20],
            acodec=acodec[:20],
            filesize=f.get("filesize") or f.get("filesize_approx"),
            note=f.get("format_note", ""),
        ))

    duration = info.get("duration") or 0

    return VideoInfoResponse(
        title=info.get("title", "Unknown"),
        thumbnail=info.get("thumbnail", ""),
        duration=duration,
        duration_string=_format_duration(duration),
        channel=info.get("channel") or info.get("uploader", "Unknown"),
        view_count=info.get("view_count"),
        upload_date=info.get("upload_date"),
        formats=formats,
    )


@app.post("/api/download")
async def download_video(req: DownloadRequest):
    """Download a video and stream it back as a file."""
    _cleanup_old_files()

    file_id = uuid.uuid4().hex[:12]
    output_template = os.path.join(DOWNLOAD_DIR, f"{file_id}_%(title)s.%(ext)s")

    format_id = req.format_id or "best"
    format_str = (
        f"{format_id}+bestaudio[ext=m4a]/{format_id}/best"
        if format_id != "best"
        else "bestvideo+bestaudio/best"
    )

    ydl_opts = {
        "format": format_str,
        "outtmpl": output_template,
        "merge_output_format": "mp4",
        "quiet": True,
        "no_warnings": True,
        "postprocessors": [
            {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"},
        ],
    }

    try:
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, _download, req.url, ydl_opts)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Download failed: {str(e)}")

    # Find the downloaded file (yt-dlp may adjust the filename)
    pattern = os.path.join(DOWNLOAD_DIR, f"{file_id}_*")
    files = glob.glob(pattern)

    if not files:
        raise HTTPException(status_code=500, detail="Download completed but file not found")

    filepath = files[0]
    filename = os.path.basename(filepath).replace(f"{file_id}_", "", 1)

    return FileResponse(
        path=filepath,
        filename=filename,
        media_type="application/octet-stream",
        background=None,  # Don't delete immediately — cleanup handles it
    )


# ---------------------------------------------------------------------------
# Blocking helpers (run in executor)
# ---------------------------------------------------------------------------

def _extract_info(url: str, opts: dict):
    with yt_dlp.YoutubeDL(opts) as ydl:
        return ydl.extract_info(url, download=False)


def _download(url: str, opts: dict):
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])


# ---------------------------------------------------------------------------
# Run directly for development
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

import yt_dlp

def fetch_formats(url):
    """Fetches and displays available formats for the provided YouTube URL."""
    ydl_opts = {
        'listformats': True,
        'quiet': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
            
            print("\n" + "="*110)
            print(f"{'ID':<10} {'EXT':<10} {'RESOLUTION':<20} {'TYPE':<12} {'CODECS (V/A)':<30} {'NOTES'}")
            print("-" * 110)
            
            for f in formats:
                fid = f.get('format_id')
                ext = f.get('ext')
                resolution = f.get('resolution') or f.get('format_note', 'N/A')
                note = f.get('format_note', '')
                vcodec = f.get('vcodec') or 'none'
                acodec = f.get('acodec') or 'none'
                
                # Determine type
                if vcodec != 'none' and acodec != 'none':
                    ftype = "Combined"
                elif vcodec != 'none':
                    ftype = "Video Only"
                elif acodec != 'none':
                    ftype = "Audio Only"
                else:
                    ftype = "N/A"
                
                if ftype != "N/A":
                    codecs = f"{vcodec[:12]}/{acodec[:12]}"
                    print(f"{str(fid):<10} {str(ext):<10} {str(resolution):<20} {ftype:<12} {codecs:<30} {note}")
            
            print("="*110)
            return True
    except Exception as e:
        print(f"Error fetching formats: {e}")
        return False

def download_video(url, format_id='best'):
    """Downloads a YouTube video using yt-dlp with a specific format."""
    
    # Check if ffmpeg is available for merging
    from yt_dlp.postprocessor.ffmpeg import FFmpegPostProcessor
    temp_ydl = yt_dlp.YoutubeDL()
    pp = FFmpegPostProcessor(temp_ydl)
    if not pp.available:
        print("\n[WARNING] FFmpeg was not found. High-quality (1080p+) downloads may have no audio or fail to merge.")
    
    # Improved format selection logic
    # If a specific ID is provided, try to merge it with best audio if it's video-only.
    # We use m4a for audio to ensure best compatibility with MP4 container.
    format_str = f"{format_id}+bestaudio[ext=m4a]/best" if format_id else "bestvideo+bestaudio/best"
    
    ydl_opts = {
        'format': format_str,
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4', # Ensures it merges into MP4 if possible
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\nStarting download using format: {format_str}")
            ydl.download([url])
            print("\nDownload completed successfully!")
    except Exception as e:
        print(f"\nAn error occurred during download: {e}")

if __name__ == "__main__":
    print("--- YouTube Video Downloader (Enhanced) ---")
    video_url = input("Enter YouTube URL: ").strip()
    
    if video_url:
        if fetch_formats(video_url):
            choice = input("\nEnter Format ID to download (or press Enter for best quality): ").strip()
            download_video(video_url, choice)
        else:
            print("Could not retrieve format list. Please check the URL.")
    else:
        print("URL cannot be empty.")


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
            
            print("\n" + "="*80)
            print(f"{'ID':<10} {'EXT':<10} {'RESOLUTION':<20} {'TYPE':<10} {'NOTES'}")
            print("-" * 90)
            
            for f in formats:
                fid = f.get('format_id')
                ext = f.get('ext')
                resolution = f.get('resolution') or f.get('format_note', 'N/A')
                note = f.get('format_note', '')
                vcodec = f.get('vcodec') or 'none'
                acodec = f.get('acodec') or 'none'
                
                # Determine type
                if vcodec != 'none' and acodec != 'none':
                    ftype = "Video+A"
                elif vcodec != 'none':
                    ftype = "Video Only"
                elif acodec != 'none':
                    ftype = "Audio Only"
                else:
                    ftype = "N/A"
                
                if ftype != "N/A":
                    print(f"{str(fid):<10} {str(ext):<10} {str(resolution):<20} {ftype:<10} {note}")
            
            print("="*90)
            return True
    except Exception as e:
        print(f"Error fetching formats: {e}")
        return False

def download_video(url, format_id='best'):
    """Downloads a YouTube video using yt-dlp with a specific format."""
    # Using format_id + bestaudio ensures we get audio if format_id is video-only.
    # The '/best' fallback handles cases where the merge string isn't valid.
    ydl_opts = {
        'format': f"{format_id}+bestaudio/best" if format_id else 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4', # Ensures it merges into MP4 if possible
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\nStarting download with format ID: {format_id if format_id else 'Default'}")
            ydl.download([url])
            print("\nDownload completed successfully!")
    except Exception as e:
        print(f"An error occurred during download: {e}")

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


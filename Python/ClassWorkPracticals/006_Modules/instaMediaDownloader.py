import instaloader
import re
import os
import getpass

def get_shortcode(url):
    """
    Extracts the shortcode from an Instagram URL.
    Works for:
    - https://www.instagram.com/p/SHORTCODE/
    - https://www.instagram.com/reels/SHORTCODE/
    - https://www.instagram.com/reel/SHORTCODE/
    - https://www.instagram.com/tv/SHORTCODE/
    """
    # Regular expression to find the shortcode after /p/, /reels/, /reel/, or /tv/
    pattern = r'/(?:p|reels|reel|tv)/([^/?#&]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

def download_media(url, username=None):
    """
    Downloads media from an Instagram URL using Instaloader.
    """
    L = instaloader.Instaloader()
    
    # Handle Login for private content
    if username:
        session_file = f"{username}_session"
        try:
            # Try to load existing session
            if os.path.exists(session_file):
                print(f"\n[INFO] Loading existing session for '{username}'...")
                L.load_session_from_file(username, filename=session_file)
            else:
                # Prompt for password securely
                password = getpass.getpass(f"Enter password for Instagram account '{username}': ")
                print(f"[INFO] Logging in as {username}...")
                L.login(username, password)
                # Save session for future use
                L.save_session_to_file(filename=session_file)
                print(f"[SUCCESS] Login successful and session saved.")
        except Exception as e:
            print(f"[ERROR] Login failed: {e}")
            print("[NOTICE] Continuing as guest (only public content will be accessible).")
            # Create a fresh instaloader instance if login fails to clear any partial state
            L = instaloader.Instaloader()

    # Extract shortcode
    shortcode = get_shortcode(url)
    if not shortcode:
        print("\n[ERROR] Could not find a valid shortcode in the URL.")
        print("Please ensure the URL is in the format: https://www.instagram.com/p/ABC123XYZ/")
        return

    try:
        print(f"\n[INFO] Fetching metadata for shortcode: {shortcode}...")
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        
        print(f"[INFO] Author: {post.owner_username}")
        print(f"[INFO] Media Type: {'Carousel' if post.mediacount > 1 else 'Single Item'}")
        
        # Download the post
        # 'target' is the folder name where files will be saved
        print(f"[INFO] Starting download...")
        L.download_post(post, target=shortcode)
        
        print(f"\n[SUCCESS] Media downloaded successfully!")
        print(f"[LOCATION] Files saved in folder: {os.path.abspath(shortcode)}")
        
    except instaloader.exceptions.LoginRequiredException:
        print("\n[ERROR] This content is private. Please run the script with your username to log in.")
    except instaloader.exceptions.ConnectionException as e:
        print(f"\n[ERROR] Connection issue: {e}")
    except instaloader.exceptions.InstaloaderException as e:
        print(f"\n[ERROR] An Instagram error occurred: {e}")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("="*50)
    print("      Instagram Media Downloader (Specialized)")
    print("="*50)
    
    insta_url = input("\nEnter Instagram Post/Reel URL: ").strip()
    
    if not insta_url:
        print("[ERROR] URL cannot be empty.")
    else:
        print("\nDo you want to log in to download private content? (y/n)")
        choice = input("Choice: ").lower().strip()
        
        user = None
        if choice == 'y':
            user = input("Enter your Instagram username: ").strip()
        
        download_media(insta_url, user)
    
    print("\n" + "="*50)
    print("             Process Completed")
    print("="*50)

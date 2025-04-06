import os
from yt_dlp import YoutubeDL

def play_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'noplaylist': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_url = next((f['url'] for f in info_dict['formats'] if f['ext'] == 'mp4'), None)
        if video_url:
            os.system(f"mpv '{video_url}'")

def main():
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    play_video(url)

if __name__ == "__main__":
    main()

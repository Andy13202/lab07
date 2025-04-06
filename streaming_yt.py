import os
from youtube_dl import YoutubeDL

def play_video(url):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'noplaylist': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_url = info_dict['formats'][0]['url']
        os.system(f"mpv {video_url}")

def main():
    # YouTube視頻URL
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # 這裡放你要播放的YouTube視頻連結
    play_video(url)

if __name__ == "__main__":
    main()

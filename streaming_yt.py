import os
from yt_dlp import YoutubeDL

def play_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'noplaylist': True,
        'geo_bypass': True,  # 嘗試繞過地區限制
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_url = info_dict['url']
        os.system(f"mpv '{video_url}'")

def main():
    # YouTube視頻URL
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # 這裡放你要播放的YouTube視頻連結
    play_video(url)

if __name__ == "__main__":
    main()

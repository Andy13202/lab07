import os
from yt_dlp import YoutubeDL

def play_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # 获取最佳视频和最佳音频，或者最佳整体质量的流
        'noplaylist': True,
        'geo_bypass': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        if 'url' in info_dict:
            video_url = info_dict['url']  # 直接获取URL
        else:
            # 如果顶层没有URL，从formats中选择一个URL
            video_url = info_dict['formats'][0]['url']  # 选择第一个格式的URL

        os.system(f"mpv '{video_url}'")

def main():
    # YouTube视频URL
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # 这里放你要播放的YouTube视频链接
    play_video(url)

if __name__ == "__main__":
    main()

import os
from yt_dlp import YoutubeDL

def play_video(url):
    ydl_opts = {
        # 选择兼容性较高的格式，确保音频和视频都能正常播放
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
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
            # 从最佳格式选择视频URL
            video_url = None
            for f in info_dict['formats']:
                if f['ext'] == 'mp4' and ('acodec' in f and f['acodec'] != 'none'):
                    video_url = f['url']
                    break

        if video_url:
            os.system(f"mpv '{video_url}'")
        else:
            print("No suitable video format found.")

def main():
    # YouTube视频URL
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # 这里放你要播放的YouTube视频链接
    play_video(url)

if __name__ == "__main__":
    main()

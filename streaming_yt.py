from pytube import YouTube
import os

def play_video(url):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    play_url = video.url
    os.system(f"mpv '{play_url}'")

def main():
    # YouTube視頻URL
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # 這裡放你要播放的YouTube視頻連結
    play_video(url)

if __name__ == "__main__":
    main()

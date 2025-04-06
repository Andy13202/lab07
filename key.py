import pafy
import os
import keyboard  # 使用keyboard庫來處理鍵盤事件

def play_video(url):
    video = pafy.new(url)
    best = video.getbest()
    play_url = best.url
    os.system(f"mpv {play_url}")

def main():
    videos = {
        '1': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',  # 例子視頻1
        '2': 'https://www.youtube.com/watch?v=xxxxxxxxxxx'   # 例子視頻2
        # 可以加更多視頻
    }
    
    print("Press the video number (1, 2) to play, press '0' to quit.")
    
    while True:
        for key in videos.keys():
            if keyboard.is_pressed(key):
                play_video(videos[key])
                while keyboard.is_pressed(key):  # 等待直到按鍵釋放，避免重複觸發
                    pass
        if keyboard.is_pressed('0'):
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()

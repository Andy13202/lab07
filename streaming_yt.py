import pafy
import os

# YouTube視頻URL
url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # 這裡放你要播放的YouTube視頻連結

# 使用Pafy獲取視頻資訊
video = pafy.new(url)

# 獲取最佳品質的視頻流
best = video.getbest()

# 獲取視頻的URL
play_url = best.url

# 使用MPV播放器播放視頻
os.system(f"mpv {play_url}")

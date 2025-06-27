# pip install yt_dlp
from yt_dlp import YoutubeDL
import os

os.environ["PATH"] += os.pathsep + "C:\\ffmpeg\\bin"

def download_video(url):
    ydl_opts={
        'format':'bv*[height<=1080][ext=mp4]+ba[ext=m4a]/b[ext=mp4]',
        'merge_output_format':'mp4',
        'outtmpl':'%(title)s.%(ext)s'
    }
    """
    YoutubeDL 이 클래스가 파일을 진짜 저장해요. 그래서 제작자가
    with 붙여서 이 코드 사용 하래요
    """
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

url = "https://www.youtube.com/watch?v=ekr2nIex040"
download_video(url)
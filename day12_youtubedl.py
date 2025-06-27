# pip install yt_dlp

def download_video(url):
    ydl_opts={
        'format':'bv*[height<=1080][ext=mp4]+ba[ext=m4a]/b[ext=mp4]',
        'merge_output_format':'mp4',
        'outtmpl':'%(title)s.%(ext)s'
    }
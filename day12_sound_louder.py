# pip install ffmpeg-python

import ffmpeg
import os
os.environ["PATH"] += os.pathsep + "C:\\ffmpeg\\bin"

input_path="C:/Users/itg/Videos/nothing_gonna_change_my_love_for_you.mp4"
output_path="C:/Users/itg/Videos/nothing_gonna_change_my_love_for_you_louder.mp4"

ffmpeg.input(input_path).output(
    output_path,
    af="volume=1.25",
    **{'c:v':'copy'}
).run()
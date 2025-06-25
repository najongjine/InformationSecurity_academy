from pydub import AudioSegment
import numpy as np
import os

def normalize_audio(audio: AudioSegment, target_dBFS=-20.0):
    change_in_dBFS = target_dBFS - audio.dBFS
    return audio.apply_gain(change_in_dBFS)

# MP3 파일이 있는 폴더
input_folder = "C:/Users/itg/Videos/mp3_original"
output_folder = "C:/Users/itg/Videos/mp3_converted"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".mp3"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        print(f"## input_path:{input_path}")
        # MP3 → AudioSegment로 로드
        audio = AudioSegment.from_mp3(input_path)

        # 볼륨 정규화 (예: -20 dBFS)
        normalized_audio = normalize_audio(audio, target_dBFS=-20.0)

        # 저장
        normalized_audio.export(output_path, format="mp3")
        print(f"{filename} 정규화 완료")

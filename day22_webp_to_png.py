import os
from PIL import Image

def convert_webp_to_png(folder_path):
    # 변환 대상 폴더가 실제로 존재하는지 확인
    if not os.path.isdir(folder_path):
        print("❌ 폴더가 존재하지 않습니다:", folder_path)
        return

    count = 0  # 변환한 이미지 수
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".webp"):
            webp_path = os.path.join(folder_path, filename)
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(folder_path, png_filename)

            try:
                with Image.open(webp_path) as im:
                    im.save(png_path, "PNG")
                print(f"✅ 변환 완료: {filename} → {png_filename}")
                count += 1
            except Exception as e:
                print(f"⚠️ 변환 실패: {filename} - {e}")

    print(f"\n총 {count}개의 .webp 파일이 PNG로 변환되었습니다.")
path="C:/Users/itg/Documents/python_test/AutoCrawler/download/Mata Mata Turtle"
# 사용 예시
convert_webp_to_png(path)  # 여기에 경로를 입력

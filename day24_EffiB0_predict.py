# 1️⃣ Colab 드라이브 마운트
from google.colab import drive
drive.mount('/content/drive')

# 2️⃣ 필요한 모듈 임포트
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import json # Import the json module here
from tensorflow.keras.applications.efficientnet import preprocess_input


# 5️⃣ 이미지 불러와서 전처리
IMG_HEIGHT = 224
IMG_WIDTH = 224

# 3️⃣ 저장된 모델 불러오기
# 3️⃣ 저장된 모델 & 클래스 이름 불러오기
model_path = '/content/drive/MyDrive/my_models/tensorflow_keras/EfficientNetB0.h5'
label_path = '/content/drive/MyDrive/my_models/tensorflow_keras/EfficientNetB0.json'
model = load_model(model_path)
print("✅ 모델 불러오기 성공!")

# 클래스 이름을 JSON에서 로딩
with open(label_path, 'r') as f:
    class_names = json.load(f)
print(f"✅ 클래스 이름 로딩 완료: {class_names}")

# 4️⃣ 사용자로부터 사진 입력받기
from google.colab import files
uploaded = files.upload()  # 사용자 업로드창 뜸

# 업로드된 파일 이름 가져오기
img_filename = list(uploaded.keys())[0]
print(f"✅ 입력된 이미지: {img_filename}")



img = image.load_img(img_filename, target_size=(IMG_HEIGHT, IMG_WIDTH))
img_array = image.img_to_array(img)
img_array = preprocess_input(img_array)  # ✅ VGG16 방식으로 전처리!
img_array = np.expand_dims(img_array, axis=0)  # 배치 차원 추가

# 6️⃣ 예측하기
predictions = model.predict(img_array)

# 예측 결과 출력
predicted_class = class_names[np.argmax(predictions)]

print(f"✅ 예측 결과: {predicted_class}")
print(f"✅ 클래스별 확률: {predictions}")

for i, prob in enumerate(predictions[0]):
    print(f"{class_names[i]}: {prob:.4f}")

# 7️⃣ 이미지도 함께 보여주기
plt.imshow(img)
plt.axis('off')
plt.title(f"Prediction: {predicted_class}")
plt.show()
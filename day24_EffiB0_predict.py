from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import json

# 모델 바꾸면 요것도 바꿔줘야함
from tensorflow.keras.applications.efficientnet import preprocess_input

IMG_HEIGHT=224
IMG_WIDTH=224

model_path='/content/drive/MyDrive/my_models/tensorflow_keras/EffiB0_test.h5'
label_path='/content/drive/MyDrive/my_models/tensorflow_keras/EffiB0_test.json'
model=load_model(model_path)

with open(label_path,'r') as f:
  class_names=json.load(f)
print(f"클래스 이름 로딩 완료:{class_names}")

# 이미지 업로드 버튼 튀어 나옴
from google.colab import files
uploaded=files.upload()

img_filename=list(uploaded.keys())[0]
print(f"입력된 이미지:{img_filename}")
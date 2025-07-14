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
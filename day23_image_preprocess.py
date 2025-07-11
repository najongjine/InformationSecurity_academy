"""
대표 폴더 만들기

train, validation 폴더 만들기

train, validation 각 폴더 안에 크롤링한 객체 이름이 붙어있는 폴더 만들기

validation엔 10~30개 나머진 train 폴더에 몰빵

"""


# 기본적인 학습 모듈 + EffiB0 모델 가져오기
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense,GlobalAveragePooling2D, Dropout
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input

from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.losses import CategoricalCrossentropy
from tensowflow.keras.optimizers import Adam

import numpy as np
import os
import json
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')
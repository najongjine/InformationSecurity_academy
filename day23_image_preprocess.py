# 기본적인 학습 모듈 + EffiB0 모델 가져오기
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense,GlobalAveragePooling2D, Dropout
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input

from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.optimizers import Adam

import numpy as np
import os
import json
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')


seed = 15
np.random.seed(seed)
tf.random.set_seed(seed)

BATCH_SIZE= 20
EPOCHS=50
IMG_HEIGHT=224
IMG_WIDTH=224

base_dir='/conent/drive/MyDrive/dataset/wierd_animals'
train_dir=os.path.join(base_dir,'train')
validation_dir=os.path.join(base_dir,'validation')
print(f"train_dir : {train_dir}")
print(f"validation_dir : {validation_dir}")
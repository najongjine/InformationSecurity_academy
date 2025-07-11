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

base_dir='/content/drive/MyDrive/dataset/wierd_animals'
train_dir=os.path.join(base_dir,'train')
validation_dir=os.path.join(base_dir,'validation')
print(f"train_dir : {train_dir}")
print(f"validation_dir : {validation_dir}")




train_ds=tf.keras.utils.image_dataset_from_directory(
    train_dir,
    label_mode="categorical",
    batch_size=BATCH_SIZE,
    image_size=(IMG_HEIGHT,IMG_WIDTH),
    shuffle=True
)
val_ds=tf.keras.utils.image_dataset_from_directory(
    validation_dir,
    label_mode="categorical",
    batch_size=BATCH_SIZE,
    image_size=(IMG_HEIGHT,IMG_WIDTH),
    shuffle=False
)
def augment(image,label):
  image=tf.image.random_flip_left_right(image)
  image=tf.image.random_brightness(image,max_delta=0.2)
  image=tf.image.random_contrast(image,lower=0.8,upper=1.2)
  image=tf.image.random_saturation(image,lower=0.8,upper=1.2)
  image=tf.image.random_hue(image,max_delta=0.05)
  return image,label

def resize_pad_preprocess(image,label):
  image=tf.image.resize_with_pad(image,IMG_HEIGHT,IMG_WIDTH)
  image=preprocess_input(image)
  return image,label

# 파이프라인 구성. 데이터증강 + reszie 전처리 한방에 처리하기
train_ds=train_ds.map(augment,num_parallel_calls=tf.data.AUTOTUNE)
train_ds=train_ds.map(resize_pad_preprocess,num_parallel_calls=tf.data.AUTOTUNE)
train_ds=train_ds.prefetch(tf.data.AUTOTUNE)

val_ds=val_ds.map(resize_pad_preprocess,num_parallel_calls=tf.data.AUTOTUNE)
val_ds=val_ds.prefetch(tf.data.AUTOTUNE)

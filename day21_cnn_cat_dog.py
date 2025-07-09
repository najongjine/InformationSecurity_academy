"""
# 데이터셋 다운로드
!wget https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip

# 압축 풀기
!unzip -q cats_and_dogs_filtered.zip


from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D
from tensorflow.keras.optimizers import RMSprop

from tensorflow.keras.preprocessing.image import ImageDataGenerator

import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
"""

"""
학습 시킬 이미지는 굉장히 깨끗해야 해요.
예를들어서 고양이를 학습시키는데, 사람이 잡고 있는 사람은 잘못 학습이 될수 있어요

컴퓨터는 사진 하나도, 조명이나 밝기가 달라지면 다른놈으로 인색해요
예를들어서 고양이가 집안에 있을때랑 밖에서 햇빛 쬐는거랑 다른 생명채로 인색해요

이런 한도끝도 없는 문제는 일일히 조명 쬐주고 햋빛 쬐주고 하면 한도끝도 없어요

이걸 해결해 주는 모듈이 있어요 
ImageDataGenerator
"""


"""
컴퓨터는 고양이가 중앙에서 조금만 벗어나도 바보라서 못알아봐요
그래서 이미지 한장을 회전도 시키고, 위치 중앙에서 벗어나기도 넣고, 좌우 반전도 시켜서
이미지 한장을 여러가지 상황으로 지가 만들어요

train_datagen= ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.3,
    height_shift_range=0.3,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)
validation_datagen=ImageDataGenerator(rescale=1./255)

train_generator=train_datagen.flow_from_directory(
    directory=train_dir,
    batch_size=BATCH_SIZE,
    shuffle=True,
    target_size=(IMG_HEIGHT,IMG_WIDTH),
    class_mode='categorical'
)
validation_generator=validation_datagen.flow_from_directory(
    directory=train_dir,
    batch_size=BATCH_SIZE,
    target_size=(IMG_HEIGHT,IMG_WIDTH),
    class_mode='categorical'
)
"""


"""
model= Sequential()
model.add(Conv2D(32, kernel_size=(3,3),padding='same'
,activation='relu',input_shape=(28,28,1)))
#model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
model.add(Conv2D(64, kernel_size=(3,3),padding='same'
,activation='relu'))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dense(10,activation='softmax'))


model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)
history=model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE
)
model.save('my_cat_dog.h5')
"""
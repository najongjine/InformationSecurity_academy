"""
# 데이터셋 다운로드
!wget https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip

# 압축 풀기
!unzip -q cats_and_dogs_filtered.zip


from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D,MaxPool2D
from tensorflow.keras.optimizers import RMSprop

#이미지 파일 읽고 조작해주는 모듈
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# numpy 밑 잡다
import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

base_dir="cats_and_dogs_filtered"
train_dir=os.path.join(base_dir,"train")
validation_dir=os.path.join(base_dir,"validation")
print(train_dir)
print(validation_dir)

# 한번에 100장의 사진을 가져와서 학습 시킨다
BATCH_SIZE= 100
# 학습 몇바퀴 시킬꺼냐
EPOCHS=100
IMG_HEIGHT=150
IMG_WIDTH=150
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
,activation='relu',input_shape=(IMG_HEIGHT,IMG_WIDTH,3)))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
model.add(Conv2D(64, kernel_size=(3,3),padding='same'
,activation='relu'))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dense(2,activation='softmax'))


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



# 정확도와 손실함수 시각화
acc =history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']
epochs_range=range(EPOCHS)
plt.figure(figsize=(8,8))
plt.subplot(2,1,1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(2,1,2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()
"""

"""
tensorflow keras cnn 은 이미지를 학습할때 100장 정도 가져와서 학습해요.
특징 필터라는 필터로 이미지를 훝어서 이미지를 파악하고,
100장의 특징백터를 에서 공통적인 부분을 보고 고양이다! 라고 학습해요.
만약, 고양이 앞모습만 보고 학습 했다면, 고양이 뒷모습은 판별을 못해요.
고양이 뒷모습을 판별 하려면 고양이 뒷모습도 천장정도 같이 학습해야 해요

또한 이미지 판별은 tensorflow / keras, Sequential conv2 만 있는게 아니에요
FunctionalParallel 기법도 있고, 특징찾는 새로운 버전의 함수들도 많아요

특히 vit 계열은 이미지를 패치로 쪼갠다음, 이미지를 문장처럼 서로의 관계를 형성한다음 파악해요
"""

"""
흑백 이미지 판별 90% 짜리를 개 고양이 판별에 써봤더니
75~80 간당간당해요

그러면 고래, 사자, 상쾡이, 자동차, 시계....
100가지 한다면 이거 모델 어떻게 구축해야할까?
이제 한도끝도 없어요
"""
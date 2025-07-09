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
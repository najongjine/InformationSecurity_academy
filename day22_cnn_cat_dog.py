# 예측
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np

model=load_model('my_cat_dog.h5')

img=image.load_img('longcat.png',target_size=(150,150))
img_array=image.img_to_array(img)/255.0
# 배치 크기 자동으로 넣어줌 (배치 크기, 높이, 너비, 채널) → 예: (1, 224, 224, 3)
img_array=np.expand_dims(img_array,axis=0)

# 예측하기
prediction=model.predict(img_array)
# 가장 큰 클래스 label 값 뽑기. 그러니깐 뭔 클래스냐
predicted_class=np.argmax(prediction[0])
# 클래스 이름이 폴더로 되어있어서 그거 이름 뽑는거
class_names=list(train_generator.class_indices.keys())
print(f"{class_names[predicted_class]}")


"""
공부삼아서 옛~~~날에 공개된 CNN(이미지 인식기)을 직접 구축해 봤어요
한번 실험으로 써보니, 이건 그냥 복불복이에요.
개같이 생긴 고양이를 그냥 개로 착각해요

그러면 또 새로운걸 공부해서 일일히 모델 구축해야되냐?
ㄴㄴㄴ
이번엔 파인튜닝 이라는 기법을 써볼거에요

어느 박사님이 이미 만들어 놓은걸 우리가 가져다가
재학습 시키는 거에요

앞부분(눈) {
model= Sequential()
model.add(Conv2D(32, kernel_size=(3,3),padding='same'
,activation='relu',input_shape=(IMG_HEIGHT,IMG_WIDTH,3)))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
model.add(Conv2D(64, kernel_size=(3,3),padding='same'
,activation='relu'))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
}
어느 박사님이 만들어놓은거 그대로 쓴다

뒷부분(판단) {
model.add(Flatten())
model.add(Dense(512,activation='relu'))
model.add(Dense(64,activation='relu'))
model.add(Dense(2,activation='softmax'))
}
뒷부분만 조금 고쳐서 쓴다
"""

python main.py --google true --naver true --full true --limit 250


"""
이미지 전처리-

OK{
    1번 사진 - 고양이 있고, 사람이 잡고 있다
    2번 사진 - 고양이 있고, 카펫에 앉아 있다
    3번사진 - 고양이 밥 먹는중
}

안좋음 {
    1번 사진 - 고양이 있고, 사람이 잡고 있다
    2번 사진 - 고양이 있고, 사람이 잡고 있다
    3번사진 - 고양이 밥 먹는중
}
"""
"""
Tensorflow는 부품 같은거
Keras 는 부품이 조립된 컴포넌트, 소단위 제품
"""

# 가져와서 학습할 이미지 양
BATCH_SIZE= 20

# 학습 횟수(문제집 몇번 풀어볼거냐)
EPOCHS=50

# 모델 만드신 박사님이 정한 이미지 사이즈
IMG_HEIGHT=224
IMG_WIDTH=224

"""
train_dir 에 있는 이미지들을 묶음처리 할수있도록 준비
이미지에 정답표도 붙여주고,
사이즈도 자동으로 맞춰준다

[고양이 이미지] ─┐
[강아지 이미지] ─┤  ─▶ Resize(224,224)
[말 이미지]   ─┘         │
                       ↓
                  [Image, Label]
                  [Image, Label]
                  [Image, Label]
                       ↓
               BATCH_SIZE 만큼 묶어서
                       ↓
                   train_ds 로 반환
"""
train_ds = tf.keras.utils.image_dataset_from_directory(
    train_dir,
    label_mode='categorical',
    batch_size=BATCH_SIZE,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    shuffle=True
)

"""
이 함수를 거치면, 이미지의 밝기, 명도, 색진함 요런것들을 살짝 변경함
"""
def augment(image,label):
  image=tf.image.random_flip_left_right(image)
  image=tf.image.random_brightness(image,max_delta=0.2)
  image=tf.image.random_contrast(image,lower=0.8,upper=1.2)
  image=tf.image.random_saturation(image,lower=0.8,upper=1.2)
  image=tf.image.random_hue(image,max_delta=0.05)
  return image,label

"""
이미지를 224x224 로 늘리거나 줄일때, 고물처럼 찌이이익 늘리지 말아라.
"""
def resize_pad_preprocess(image,label):
  image=tf.image.resize_with_pad(image,IMG_HEIGHT,IMG_WIDTH)
  image=preprocess_input(image)
  return image,label


"""
train_ds (image_dataset_from_directory) 에서 이미지마다 답안지를 붙였다.
얘가 답안지도 가지고 있다.
답안지에 있는 이름들 뽑아 와라
"""
class_list = train_ds.class_names

"""
train_ds (image_dataset_from_directory) 에 있는 이지미들을 augment 함수를
거치도록 해라
"""
train_ds = train_ds.map(augment, num_parallel_calls=tf.data.AUTOTUNE)


"""
mnist 손글씨랑, 개고양이 모델쌓기 할때, /255 했던기억이 있을거에요
그건 sequencial, Conv2d maxpooling 함수 만든 박사님이 255로 나누하고 해서 그렇게 한거고,
이번에는 EffiientNetB0 모델을 우리가 갔다 쓰고 있어요.
EffiientNetB0 모델을 만든 박사님이 이미지 데이터가 numpy 기준으로
-1 ~ 1 사이로 되야 된데요.
그걸 우리가 직접 하면 너무 힘들어요. 그래서 train_ds 모듈을 만든 박사님이
-1 ~ 1 로 자동으로 바꿔주는 함수를 만들어놔서, 그걸 갔다 쓴거에요
"""
train_ds = train_ds.prefetch(tf.data.AUTOTUNE)
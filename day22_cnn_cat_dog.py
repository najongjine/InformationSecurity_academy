# 예측
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

model=load_model('my_cat_dog.h5')

img=image.load_img('cat.png',target_size=(150,150))
img_array=img.img_to_array(img)/255.0
# 배치 크기 자동으로 넣어줌 (배치 크기, 높이, 너비, 채널) → 예: (1, 224, 224, 3)
img_array=np.expand_dims(img_array,axis=0)

# 예측하기
prediction=model.predict(img_array)
# 가장 큰 클래스 label 값 뽑기. 그러니깐 뭔 클래스냐
predicted_class=np.argmax(prediction[0])
# 클래스 이름이 폴더로 되어있어서 그거 이름 뽑는거
class_names=list(train_generator.class_indices.keys())
print(f"{class_names[predicted_class]}")
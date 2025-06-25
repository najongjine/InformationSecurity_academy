import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 이미지 열기
img= Image.open('test1.png').convert('RGB')
img_np=np.array(img)

# 좌우반전: 열(가로축) 순서를 뒤집는다
flipped=img_np[:,::-1,:]

plt.subplot(1,2,1)
plt.title("original")
plt.imshow(img_np)

plt.subplot(1,2,2)
plt.title("flipped")
plt.imshow(flipped)
plt.show()
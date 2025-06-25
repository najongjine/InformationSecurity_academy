import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 흑백으로 바꾸기
img= Image.open('test1.png').convert('L')
img_np=np.array(img)

# 반전 이미지 만들기
inverted=255-img_np

plt.subplot(1,2,1)
plt.title("원본 이미지")
plt.imshow(img_np,cmap='gray')

plt.subplot(1,2,2)
plt.title("반전 이미지")
plt.imshow(inverted,cmap='gray')
plt.show()
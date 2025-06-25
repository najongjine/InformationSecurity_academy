import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 이미지 열기
img= Image.open('test1.png').convert('RGB')
img_np=np.array(img)

# 발기 증가. RGB 각 채널에 50씩 더함
brighter=img_np+50

brighter=np.clip(brighter,0,255).astype(np.uint8)

plt.subplot(1,2,1)
plt.title("original")
plt.imshow(img_np)

plt.subplot(1,2,2)
plt.title("brighter")
plt.imshow(brighter)
plt.show()
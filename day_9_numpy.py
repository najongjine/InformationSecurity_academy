"""
https://wildojisan.tistory.com/64
- react 만든후 vercel에 올리기

pip install numpy
"""


import numpy as np

a=np.array([1,2,3,4])
list1=[1,2,3,4]

a+=1
#list1+=1

#print(f"a:{a}")
#print(f"list1:{list1}")

a=np.array([1,2,3])
b=np.zeros((2,3))
c=np.ones((3,3))
d=np.arange(0,10,2)
f=np.random.rand(2,3)

a=np.array([1,2,3])
b=np.array([10,20,30])

a=np.array([
    [1,2,3],
    [4,5,6]
])

# pip install matplotlib
import matplotlib.pyplot as plt
image = np.zeros((28,28))
#print(image)

# 흑백 이미지로 보여줘
#plt.imshow(image,cmap="gray")
#plt.title('28*28 black image')
#plt.axis('off')
#plt.show()


"""
numpy 에서 Shape은 단순 수학으로 설명하면
배열의 생김새를 뜻해요.
1차원이냐, 2차원이냐, 3차원이냐, 4차원이냐

하지만, 사람 입장에선, 쓰이는 AI 모델에 따라서
혹은 해결하려는 문제에 따라서 해석이 달라져요
cnn2d( my_numpy )

정리하면, numpy는 컴퓨터가 알아 먹을수 없는
이미지, 문장, 오디오 같은 데이터를
억지로 숫자로 만든거에요

그래야 컴퓨터에서 표현이 되니까요
"""

color_img = np.zeros((100,100,3))
color_img[0:50,0:50]=[0.4,0.4,0.2]
color_img[0:50,50:100]=[0,1,0]
color_img[50:100,50:100]=[1,1,1]
#print(color_img)
#plt.imshow(color_img)
#plt.title('100*100 color image')
#plt.axis('off')
#plt.show()

"""
numpy 는 이해 안가도 슬퍼하지 마세요.
저희가 GPT 모델을 만들지 않는이상, 이해 안가도 괜찬아요
진짜 AI 응용이나 활용에선 GPT한테 데이터를 컴퓨터가 알아먹을수 있는
숫자로 만들라고 시키거나, 다른 툴같은거 써요(예: ImageGenerator, Tokenizer)
"""

a=np.array([1,2,3,4,5,6])
#print(a.shape)

b=a.reshape(2,3)
#print(b)

"""
reshape을 하는 이유:
인공지능은 수많은 함수들이 있어요
어떤 함수는 3차원 shape을 원하고
어떤 함수는 1차원 shape을 원해요
그래서 거기에 맞춰주기 위해서 reshape을 써요

reshape은 행렬의 모습만 바꾸는거고,
안의 숫자 데이터는 바꾸지 않아요
"""
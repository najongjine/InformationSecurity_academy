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
print(f"a:{a}")
print(f"b:{b}")
print(f"c:{c}")
print(f"d:{d}")
print(f"f:{f}")
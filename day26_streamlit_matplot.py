"""
pip install streamlit
"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 제목
st.title("Matplot 되나 테스트 해보기")

# 가짜 데이터
x = np.linspace(0,10,100)
print(f"x:{x}")
y=np.sin(x)
print(f"y:{y}")

# 그래프 그리기
fig, ax=plt.subplots()
ax.plot(x,y,label='sin(x)',color='blue')
ax.set_tile("sine graph")
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.legend()

st.pyplot(fig)
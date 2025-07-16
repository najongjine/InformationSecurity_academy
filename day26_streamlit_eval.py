"""
pip install streamlit
"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#text1="1+1/(2^2*3)**2/1.5"
#result=eval(text1)
#print(result)

"""
저 계산기를 streamlit으로 구현해보기
"""

st.title(" 저는 streamlit 이에요")

# python 으로 치면 string 화면에 출력
st.write("저 웹사이트 아니에요")

# python 으로 치면 키보드 입력받기
text1=st.text_input("수식을 입력하세요") # 1+1
if text1:
    """
    eval 이 계산기. result 가 정답이 담긴 바구니
    """
    result=eval(text1)
    # python 으로 치면 string 화면에 출력
    st.write(f"정답 : {result}")
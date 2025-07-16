"""
pip install streamlit
"""

import streamlit as st

# 제목
st.title(" 저는 streamlit 이에요")

# python 으로 치면 string 화면에 출력
st.write("저 웹사이트 아니에요")

# python 으로 치면 키보드 입력받기
text1=st.text_input("오늘 날씨는 어때요?")
if text1:
    # python 으로 치면 string 화면에 출력
    st.write(f"오늘 날씨는 : {text1}")

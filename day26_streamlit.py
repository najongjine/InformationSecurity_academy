"""
pip install streamlit
"""

import streamlit as st

st.title(" 저는 streamlit 이에요")
st.write("저 웹사이트 아니에요")

text1=st.text_input("오늘 날씨는 어때요?")
if text1:
    st.write(f"오늘 날씨는 : {text1}")

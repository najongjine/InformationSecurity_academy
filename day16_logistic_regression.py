import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt



"""
Logistic regression -
Y or N 로 분류하는 기법

실제 사용할수 있는 사례:

개 고양이 분류,
스팸 판별기
고객 이탈 예측
대출 심사
의료 진단

"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# CSV 파일 불러오기
df = pd.read_csv("medical_diagnosis.csv", encoding="utf-8")

X= df[["나이","혈압","콜레스트롤","유전자이상여부"]]
y=df['질병여부']
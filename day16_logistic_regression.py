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

X= df[["나이","혈압","콜레스테롤","유전자이상여부"]].values
y=df['질병여부'].values

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

model=LogisticRegression()
model.fit(X_train,y_train)

"""
정확도 0.83 == 83%
인공지능에서 70~80는 잘나온거.
100% 오히려 0%에 가까움. 왜냐면 과적합이 발생한것
과적합은 사람으로 치면 시험공부 하는데, 문제집에 너무 열중한 나머지 문제집을 통채로 외우고,
문제집에 나오거랑 조금이라도 틀리면 과민반응으로 틀리게 행동하는거
"""
print(f"정확도: {model.score(X_test,y_test)}")

age=55
bloodpressure=135
colestroll=240
gene_malf=0
new_person=np.array([[age,bloodpressure,colestroll,gene_malf]]) 
predict=model.predict(new_person)
predict(f"질명 예측 결롸: {predict}")
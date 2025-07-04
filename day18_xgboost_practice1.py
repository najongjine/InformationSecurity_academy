import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error

np.random.seed(42)
data_size=500

#기온 0~35c
temperature = np.random.uniform(0,35,data_size)

#습도 20~90%
humidity=np.random.uniform(20,90,data_size)

#에너지 사용량
energy_usage=temperature*2+humidity*1.5+np.random.normal(0,5,data_size)

"""
xgb.XGBRegressor
요걸 이용해서 새로운 temperature, humidity 를 받아서 
에너지 사용량을 예측해 보세요
"""
X=pd.DataFrame({
    "temperature":temperature,
    "humidity":humidity
}).values

"""
X=pd.DataFrame({
    "temperature":temperature,
    "humidity":humidity
})
     temperature   humidity
0      13.108904  68.871320
1      33.275001  57.526746
2      25.619788  41.666933
3      20.953047  76.965651
...

X=pd.DataFrame({
    "temperature":temperature,
    "humidity":humidity
}).values
.values 붙이면
[[13.10890416 68.87131998]
 [33.27500072 57.52674564]
 [25.61978796 41.66693314]
 ...
 .values 붙이면 pandas 바로 numpy 로 변환되고, numpy 는 인공지능이 좋아한다
"""
y=energy_usage

X_train,X_text,y_train,y_test=train_test_split(X,y,test_size=0.3)

model=xgb.XGBRegressor()
model.fit(X_train,y_train)

# 정확도 어쩌구 skip... 이건 걍 gpt 한테 달라고 해도 충분

new_X=pd.DataFrame({
    "temperature":[0],
    "humidity":[5]
}).values
predicted=model.predict(new_X)
print(f"전력 사용량: {predicted}")



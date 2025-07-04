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

# 종가 모음(Close)
close=np.random.uniform(100,200,data_size)

# 거래량 모음
volume=np.random.uniform(1_000_000,5_000_000,data_size)

# 5일 이동 평균선
ma_5=close+np.random.uniform(-2,2,data_size)

# 10일 이동평균선
ma_10=close+np.random.uniform(-3,3,data_size)

#변동성
volatility=np.random.uniform(1,5,data_size)

# RSI(0~100)
rsi=np.random.uniform(30,70,data_size)

# 내일 종가(타겟)
next_close=close+np.random.uniform(-3,3,data_size)

X=pd.DataFrame({
    "close":close,
    "volume":volume,
    "ma_5":ma_5,
    "ma_10":ma_10,
    "volatility":volatility,
    "rsi":rsi,
    "revenue":np.random.uniform(3000,7000,data_size), # 매출
    "net_income":np.random.uniform(100,500,data_size), #순이익
    "debt_ratio":np.random.uniform(20,80,data_size), # 부채비율
    "per":np.random.uniform(8,20,data_size) # PER
    
}).values
y=next_close

# 학습,테스트 데이터 나누기
X_train,X_text,y_train,y_test=train_test_split(X,y,test_size=0.3)

# 학습
model=xgb.XGBRegressor()
model.fit(X_train,y_train)

# 테스트 데이터로 한번 돌려보기
y_pred=model.predict(X_text)
# 한번 돌려본 결과랑, 진짜 정답이랑 비교
mse=mean_squared_error(y_test,y_pred)
print("평균제곱오차:",mse)


new_data=pd.DataFrame({
    "close":[150],
    "volume":[2500000],
    "ma_5":[151],
    "ma_10":[149],
    "volatility":[2.5],
    "rsi":[50],
    "revenue":[5000], # 매출
    "net_income":[300], #순이익
    "debt_ratio":[40], # 부채비율
    "per":[12] # PER
    
}).values

new_pred=model.predict(new_data)
print("예측한 종가:",new_pred[0])
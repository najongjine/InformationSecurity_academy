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

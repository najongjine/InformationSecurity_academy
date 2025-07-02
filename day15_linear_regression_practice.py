import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# GDP 값 (1만~6만)
gdp = [
    15000, 23000, 32000, 40000, 50000,
    12000, 45000, 38000, 28000, 55000
]

# 실업률 값 (2~12)
unemployment = [
    4.5, 6.0, 3.2, 8.0, 5.5,
    10.0, 4.0, 7.2, 9.0, 2.5
]

# 소비지출 값 (가상의 계산)
# 소비지출 = 0.5 * GDP - 2000 * 실업률 + 50000 + noise
consumption = [
    0.5 * gdp[i] - 2000 * unemployment[i] + 50000 + np.random.normal(0,3000)
    for i in range(len(gdp))
]

df = pd.DataFrame({
    "GDP": gdp,
    "Unemployment": unemployment
})
X = df.values
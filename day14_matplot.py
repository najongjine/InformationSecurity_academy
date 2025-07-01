"""
pandas 이게 데이터 읽어서
흑백 화면에서 테이블 형태로 보여주던놈

df = pd.read_csv('test1.csv')
print(df)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
"""

"""
matplot - png 로 그래프 보여주기. 실시간 x

pip install matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np

"""
[0, 6] == list type
np.array() == numpy type으로 변형 시켜주는놈
"""
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

"""
.plot() 은 matplot 보여주기 하기전에 셋팅 해주는 함수. 값을 배개변수로 받음
"""
plt.plot(xpoints, ypoints)
# 보여주기
plt.show()
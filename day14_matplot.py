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
#plt.plot(xpoints, ypoints)
# 보여주기
#plt.show()

xpoints = np.array([0, 8,10,30])
ypoints = np.array([3, 8, 1, 10])

#plt.plot(xpoints,ypoints)
#plt.show()

"""
plt.plot(xpoints,ypoints) 함수 안에, 라인 스타일, 컬러를 정해줄수 있다

plt.plot(ypoints, 'o:r') :
꺽임 부분 o 모양으로, 선은 점선(dot) 모양으로, 색상은 빨강

plt.plot(ypoints, '*--m') :
꺽임 부분은 별 모양, 선은 dash 스타일선, 색상은 magenta

plt.plot(ypoints, linewidth = '20.5'), plt.plot(ypoints, '*--m',linewidth = '20.5'):
linewidth 는 선의 굵기 정하기
"""


y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()
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

#plt.plot(y1)
#plt.plot(y2)

#plt.show()



x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

# 요렇게 한쌍씩 묶어서 하는 스타일도 있고
#plt.plot(x1,y1)
#plt.plot(x2,y2)

# 아니면 한줄에 다하기
#plt.plot(x1,y1,x2,y2)
#plt.show()


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

#plt.plot(x, y)

#plt.title("Sports Watch Data")
# 그래프에서 x 축에 설명 넣어주기. 한글 쓰면 깨짐
#plt.xlabel("Average Pulse")
# 그래프에서 y 축에 설명 넣어주기. 한글 쓰면 깨짐
#plt.ylabel("Calorie Burnage")
#plt.show()


"""
지금 plt 모듈을 쓰고 있음
plt.뭐뭐() 이렇게 나온놈들은 plt 의 내장 함수들임

이말은 좀 고급 개념으로 말하자면, matplot으로 할수있는 기능들은
plt. 뭐뭐뭐 이렇게 나온 놈들로 한정됨
이걸 우리가 가진 핸들 이라고 한다
"""



x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#plt.title("Sports Watch Data", fontdict = font1)
#plt.xlabel("Average Pulse", fontdict = font2)
#plt.ylabel("Calorie Burnage", fontdict = font2)

#plt.plot(x, y)
#plt.show()


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

#plt.plot(x, y)

# 그래프에 그리드 그리기
#plt.grid()

#plt.show()


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

#plt.plot(x, y)

# 그리드에 스타일을 부여 하는 방법
#plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

#plt.show()


x = [1, 2, 3, 4, 5]
y1 = [10, 15, 13, 17, 20]
y2 = [12, 14, 11, 19, 22]

"""
.plot() 함수에 label='뭐뭐' 매개변수를 주면, 각 그래프 라인당 설명을 부여할수 있다
"""
plt.plot(x, y1, label='Series A')
plt.plot(x, y2, label='Series B')

plt.legend()
plt.show()
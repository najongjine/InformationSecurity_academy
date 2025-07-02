import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# pandas 로 csv 읽기
#df=pd.read_csv("car_gasoline.csv")
#print(df)

# pandas 에서 weight, engine_size 값만 뺀다음, numpy 2차원 배열화
#X=df[["weight","engine_size"]].values #학습
# 연비를 1차원 numpy 시킴
#y=df["fuel_efficiency"].values #결과, 정답

"""
df[["weight","engine_size"]] 요건
csv 에서 필요한 칼럼만 뽑았는데, 2개 이상의 칼럼은
일려로 쫙 펴서 보여주면 데이터 섞인 에러니깐
2차원으로 테이블 형태로 보여줘라

.values 이건 AI 는 완전한 백터 형태가 필요하니
바로 백터화 시켜라
"""

# LinearRegression 이라는 누가 이미 만들어 놓은거 가져옴
#model=LinearRegression()
#모델에다가 학습데이터와 정답을 같이 줌 학습끝
#model.fit(X,y)

# 차ㅣ 무게가 1500kg 일시
#weight_input = 1500
# 엔진 크기가 2L
#engine_input=2.0

# (1, -1)의 의미 행은 1개, column 은 자동계산. 2차원 행렬
#X_input=np.array([weight_input,engine_input]).reshape(1,-1)
#X_input = np.array([[weight_input, engine_input]])

#predicted_fuel=model.predict(X_input)[0]
#print(f"예상 연비: 1리터로 {predicted_fuel} km 갈수 있습니다")



# 예제 데이터: 집 크기 (㎡)
house_size = np.array([30, 40, 50, 60, 70, 80, 90, 100])

# 가격 = 면적 * 50 + 랜덤 노이즈
np.random.seed(42)  # 랜덤 고정
price = house_size * 50 + np.random.randint(-200, 200, size=house_size.shape)

# 데이터 확인
print("집 크기:", house_size)
print("가격:", price)
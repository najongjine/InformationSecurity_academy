import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

"""
XGBoost 는 기존 그래프 그리는 모델들과 달리
if 문을 지가 동적으로 연동시켜서 만들기 때문에 굉장히 강력해요
그래서 {숫자,숫자,숫자,... } = 결과
이런 문제는 얘가 거진 다 해먹을수 있어요
"""

# 2. 가상 데이터 생성 (예시)
np.random.seed(42)
data_size = 200

# 과일 크기 (cm)
size = np.random.uniform(5, 10, data_size)
# 색 (1=연함, 2=보통, 3=진함)
color = np.random.randint(1, 4, data_size)
# 당도 (Brix)
sweetness = np.random.uniform(8, 15, data_size)
# 무게 (g)
weight = np.random.uniform(150, 300, data_size)

# 품질 등급 (1, 2, 3)
# 간단히 규칙을 만들어서 라벨 생성
# (당도+색+크기 합이 클수록 높은 등급)
quality_score = sweetness + color*2 + size
labels = []
for score in quality_score:
    if score >= 23:
        labels.append(1)  # 1등급
    elif score >= 20:
        labels.append(2)  # 2등급
    else:
        labels.append(3)  # 3등급

#################### 데이터 임의로 생성 #########################

df=pd.DataFrame({
    "size":size,
    "color":color,
    "sweetness":sweetness,
    "weight":weight,
    "grade":labels
})

X=df[["size","color","sweetness","weight"]]
y=df['grade'] -1

X_train,X_test,y_train,y_test=train_test_split(X.values,y.values,test_size=0.3,random_state=42)

# 정답이 여러개일때 softmax 기법을 써요. 정답이 3개
# 정답은 1등급 2등급, 3등급
model=xgb.XGBClassifier(objective="multi:softmax",num_class=4)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"accuracy: {accuracy}")

new_fruit=pd.DataFrame({
    "size":[8],
    "color":[3],
    "sweetness":[14],
    "weight":[250]
}).values

new_pred=model.predict(new_fruit)
print(f"과일등급:{new_pred[0]+1}")

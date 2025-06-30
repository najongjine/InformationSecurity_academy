"""
pip install pandas
"""

import pandas as pd

"""
dictionary : 
무조건 {} 나오고
안에 {'키'} 나오고
{'키': 값} 이런형태를 가지고 있다
값은 무조건 list여야 한다
각 리스트 갯수도 서로 같아야한다

이 자료구조 법칙을 어기면 DataFrame() 함수는 작동을 안한다
"""
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2],
  'data2': [3, 7, 2],
}

"""
dictionary를 pandas로 읽는건, 무조건 
pandas.DataFrame(mydataset)
이 코드로 정해져있다

myvar = pandas.DataFrame(mydataset)
"""


#print(myvar)







"""
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 

DataFrame or Series을 통해서 dictionary의 값을 table 형태로 보기
column 은 집값
row 의 이름은 년도

data = {
  "집값": [50, 40, 45,55]
}

df = pd.DataFrame(data, index = [2025, 2024, 2023,2022])
"""



"""
성별 1-여성 2-남성

1	대학원 (Graduate school)
2	대학교 (University)
3	고등학교 (High school)
4	기타 (Others)

1	기혼 (Married)
2	미혼 (Single)
"""
df = pd.read_csv('test1.csv')
df=df[['LIMIT_BAL', 'SEX','EDUCATION','MARRIAGE','AGE']]
# 조건 필터링
df = df[
    (df['SEX'].isin([1, 2])) &
    (df['EDUCATION'].isin([1, 2, 3, 4])) &
    (df['MARRIAGE'].isin([1, 2]))
]

#print(df) 


filtered1=df[df['LIMIT_BAL'] <=0]


products = [
        {
            "product_id": 1,
            "name": "Wireless Mouse",
            "price": 19.99,
            "stock": 120,
            "category": "Electronics"
        },
        {
            "product_id": 2,
            "name": "Mechanical Keyboard",
            "price": 49.99,
            "stock": 85,
            "category": "Electronics"
        },
        {
            "product_id": 3,
            "name": "Water Bottle",
            "price": 12.50,
            "stock": 200,
            "category": "Home & Kitchen"
        },
        {
            "product_id": 4,
            "name": "Yoga Mat",
            "price": 25.00,
            "stock": 60,
            "category": "Sports"
        },
        {
            "product_id": 5,
            "name": "Bluetooth Speaker",
            "price": 35.75,
            "stock": 45,
            "category": "Electronics"
        },
    ]

df2 = pd.DataFrame(products)

print(df2)
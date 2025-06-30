"""
pip install pandas
"""

import pandas

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
"""
myvar = pandas.DataFrame(mydataset)

print(myvar)
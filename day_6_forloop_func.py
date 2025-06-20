"""
https://wildojisan.tistory.com/35

반복문-
말 그대로 내가 정한 횟수만큼 똑같은 코드를
반복해요

break : loop 강제 종료. 시스템 종료 X

"""

# 이건 break 때문에 아예 실행 안함
for i in range(3):
    break
    print("loop 가 돌아요")
    pass

for i in range(99):
    if i==1:
        break
    #print(f"forloop 가 돌아요. i:{i}")
    pass

for i in range (3):
    if i==1:
        continue
    #print(f"i:{i}")
    pass

#print(f"forloop 밖이에요")


"""
함수

def 함수이름():
    내용

def 함수이름(매개변수):
    내용

매개변수 : 함수를 정의할때 쓰이는 기능
변수 이름 정하고 선언하는거와 비슷한데,
호출할때 우리가 값을 정해줄수 있다

def 함수이름():
    내용..
    return x

def 함수이름(매개변수):
    내용...
    return x
"""

def myfunc():
    return 1

mynum=myfunc()
#print(mynum)

def myfunc2(a,b):
    return a+b

mynum=myfunc2(1,2)
print(mynum)


"""
재귀함수 -
이건 실전에서는 안써요. 너무 위험해서
하지만 시험에선 꼭 나와요

def recFunc(a):
    if a<=0:
        return a
    a-=1
    recFunc(a)
"""

def recFunc(a):
    print(f"a:{a}")
    if a==0:
        return a
    a-=1
    recFunc(a)

#recFunc(3)

"""
1. 숫자를 키보드로 부터 입력 받고, 홀수면 "홀수입니다"
짝수면 "짝수입니다"
출력하기
x= input("숫자를 입력해주세요:")

2. 재귀함수 풀어보기( 손으로 쓰면서)
"""
def fsum(a):
    if a<=1:
        return a
    return a+fsum(a-1)

tsum=fsum(5)
print(tsum)


num1=0
while True:
    try:
        #num1=int(input("숫자를 입력해 주세요:")) # 2
        break
        pass
    except:
        print(f"\n 숫자만 입력해 주세요!!")
        pass
    pass
if num1 % 2==0:
    #print(f"짝수 입니다")
    pass
else:
    #print(f"홀수 입니다")
    pass


"""
1. 숫자를 입력 받고, 그 숫자가 소수인지(1 빼고, 자기 자신이랑 나눴을때만 나머지가 0)
예: 3,5,7,11,13 ...
판별하기

2. 재귀함수
"""
def count_ones(s):
    if len(s) == 1:
        return 1 if s == '1' else 0
    mid = len(s) // 2 # 3/2 == 1
    return count_ones(s[:mid]) + count_ones(s[mid:])

print(f"count_ones: {count_ones("101110")}")


def fPrimeNum(a):
    bPrimeNum=True
    for i in range(2,a):
        bPrimeNum=False
        break
    return bPrimeNum

num1=7
#num1=int(input("숫자를 입력하세요:"))
bPrimeNum=fPrimeNum(num1)
if bPrimeNum:
    print(f"{num1} 은 소수 입니다")
else:
    print(f"{num1} 는 소수가 아닙니다")

"""
내장함수, 외장함수 -
이것들은, 누군가가 이미 만들어 놓은거 갔다 쓰는거에요
스타일과 사용 방법은 만든 사람마다 다 달라요

*백화점세트 - 진짜 좋아요. 너무 쉽고 편해요

*철물점세트 - 이게 짜증나요. 사용법 읽어보면서 해야되요
"""
mytype=""
#mytype=input("수학 수식을 넣어주세요:")
#result=eval(mytype)
#print(f"{mytype}:{result}")

# 모듈 : 다른 사람이 만든 코드 덩어리.  함수도 있음
from random import shuffle
list1=[]
for i in range(1,46):
    list1.append(i)
shuffle(list1)
#print(f"추첨번호: {list1[0:6]}")

#* i 1 이랑 pop 1, 이랑 곱하기
#* forloop 입장에선 두번째임. [2,3,4,5] 에서 3을 택. i 가 3
# pop은 2     2*3
#* forloop 입장에선 3번째임. [3,4,5] 에서 5을 택. i 가 5
# pop은 3     3*5
list1=[1,2,3,4,5]
result=[list1.pop(0) * i for i in list1]
print(result) # 1,6,15

1
2
3
list1=[1,2,3,4,5]
result=[list1.pop(0) for i in list1]
print(f"result:{result}") # 1,2,3

"""
pop 기준이랑 i의 index 접근이랑 따로놀음
forloop 먼저실행, 그다음 pop이 실행
1.for 에 list1 이 담기고, list1[0] 값을 pop list1=[2,3,4,5]
list[0] pop     list1=[3,4,5]
list[0] pop     list1=[4,5]
"""

"""
자바랑 파이썬은 포인터가 없으니
int, string, bool 얘네들은 복사

list는 참조
"""

"""
클래스-
파이썬 생태계에선, 모듈 만드는 사람 말고는 잘 안쓰임

"""
# 기본 틀
class MyClass:
    def __init__(self):
        pass

class Customer:
    def __init__(self,name,birthdate,rank):
        self.name=name
        self.birthdate=birthdate
        self.rank=rank
        pass

myclass1=MyClass()
customer1=Customer("박종진","1987","일반고객")
print(customer1.name)
print(customer1.birthdate)


"""
클래스- 붕어빵 틀 기계

객체- 붕어빵

이렇게 쉬우면 얼마나 좋겠어요... 하지만 실전에서 클래스를
써보면 너무 어려워요

클래스는 대부분 자바,c#,c++ 얘네가 쓰고
자바스크립트, 파이썬은 잘 안써요
"""
class Animal:
    def __init__(self):
        pass
    def bark(self):
        print("Animal으르릉...")
class Animal2:
    def __init__(self):
        pass
    def bark(self):
        print("Animal2으르릉...")
class Dog(Animal,Animal2):
    def __init__(self,name):
        self.name=name
    def run(self):
        print("달려가요~~")
        
dog1=Dog("보더콜리")
dog1.bark()
dog1.run()
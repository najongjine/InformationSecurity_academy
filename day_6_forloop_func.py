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
    mid = len(s) // 2
    return count_ones(s[:mid]) + count_ones(s[mid:])

#print(count_ones("101110"))


def fPrimeNum(a):
    bPrimeNum=True
    for i in range(2,a):
        bPrimeNum=False
        break
    return bPrimeNum


num1=int(input("숫자를 입력하세요:"))
bPrimeNum=fPrimeNum(num1)
if bPrimeNum:
    print(f"{num1} 은 소수 입니다")
else:
    print(f"{num1} 는 소수가 아닙니다")
"""
https://wildojisan.tistory.com/35

반복문-
말 그대로 내가 정한 횟수만큼 똑같은 코드를
반복해요

for i in range(5):
    print("안녕", i)

i = 1
while i <= 5:
    print(i)
    i += 1  # i를 1씩 증가시킴
"""

"""
for loop 가 제일 많이 쓰여요
왜냐면, if문과 비슷하게, 조건이 true 여야 반복하는데,
for loop는 조건을 처음부터 지정합니다
즉, 무한루프에 빠질 일이 없어요
"""
for i in range(3):
    #print(f"{i}")
    pass

for i in range(2,10):
    #print(f" i in range(2,10): {i}")
    pass

list1=["사과","바나나","딸기"]
for e in list1:
    #print(e)
    pass
"""
시험문제 낼때 빼고는 잘 안써요.
왜냐면, 조건을 잘못 쓰면, 계속 True 상태가 되서
무한루프에 빠져요
"""
i=0
while i<3:
    #print(i)
    #i=i+1, i+=1
    i+=1
    pass

"""
구구단 출력하기
2*1=2
2*2=4
...
9*9=81

if:
    if:
    
for i in range(3):
    for i in range(3):
"""

for i in range(2,10):
    for j in range(1,10):
        #print(f"{i} * {j} = {i*j}")
        pass

# 이거 오름차순으로 정렬하기
"""
이중 for 문으로 해결 가능.
numbers[i] 랑 numbers[i+1] 이랑 비교후, i 가 더 크면 

swap 방법 1
temp= numbers[i]
numbers[i]=numbers[i+1]
numbers[i+1]=temp

swap 방법 2
numers[j], numers[j + 1] = numers[j + 1], numers[j]
"""
                                                    #12
numers=[2,54,22,7,9,4,23,5,78,4,23455346534,43342,43567]
numers[12]
for i in numers:
    pass


for i in range(len(numers)): # range(13) 이랑 같음 13 * 13
    for j in range(len(numers)):
        try:
            if numers[j] > numers[j+1]:
                numers[j],numers[j+1]=numers[j+1],numers[j]
        except:
            pass
        pass
#print(numers)

"""
try:
    pass
except:
    pass

이건 예외처리 코드입니다
try 안쪽에서 코드가 에러가 나면 무조건 except 로 빠집니다.
if
else
랑 약간 비슷합니다
"""

sdfsdsd=10

if 10:
    pass


"""
들여쓰기 (tab)
파이썬은 들여쓰기에 매우 민감함.
들여쓰기가 있으면, 들여써진 코드는 부모 코드가 있다는 뜻임

if True :
    들여쓰기
elif True :
    들여쓰기
else :
    들여쓰기

for i in range(3):
    들여쓰기

try:
    들여쓰기
except:
    들여쓰기

if True:
    if True:
        들여쓰기 2번 해야 안쪽 if문 내용 실행
    들여쓰기 한번은 위쪽 if문 내용
"""


"""
forloop 를 정리하자면,
얘도 보기엔 단순해 보이지만, 실제 코드 돌아가는거 생각하면 어지러움
for
    for 
이렇게 있으면 상당히 복잡해짐.
그래서 실전에선 저렇게 중첩 잘 안함

실전에서 forloop로 할수 있는건 굉장히 많음

* 쇼핑몰 만들때 제품 보여주기
* AI 는 데이터 전처리 할때
* 서버는 파일을 url 링크로 바꿀때
* 게임 엔진 만들때도 필수
"""

"""
함수-

함수는 코드 뭉탱이를 한곳에 모아놓아서, 
코드 분석 하기 싫은 사람도 갔다 쓰기만 하면 됨

def 이름지어주기():
    내용...

함수는 만든 다음엔, 그냥 실행 안됨
꼭 내가 호출을(사용을) 해줘야함
"""
# 함수 선언
def print_hello():
    print(f"hello")
    pass

# 함수 사용하기(호출)
print_hello()

"""
함수는 매개변수를 받을수도 있고,
값을 퉤 뱉을수도 있습니다
"""

# a,b 가 매개변수
def sum(a,b):
    c=1
    # 리턴값. 퉤 뱉은값
    return a+b

"""
mod 연산 (%) 하는 함수를 만들어 보세요.
매개변수 2개를 받아서 mod 연산을 하면 됩니다.
"""

def mod(a,b):
    #print(f"{a%b}")
    return a%b

print(mod(2,3))
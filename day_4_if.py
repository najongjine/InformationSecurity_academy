# 여기서 적는건, 컴퓨터가 무시함
"""
여기서 적는건, 컴퓨터가 무시함
몇줄 이상 되고 상관 없음
"""
"""
그러면 이 컴퓨터란 놈은 대체 뭘 읽어요????

수식만 읽을수 있어요
"""






"""
if 문
https://wildojisan.tistory.com/13

if 조건:
    실행할 코드
if(조건):
    실행할 코드

핵심은 엄청 간단함
조건 수식이 True(참) 이면 안쪽에 있는 코드를 수행함

if문은 인공지능에 아주 기초
if문은 모든 분야에서 다쓰임

서버, 웹, 앱, 게임, iot... 다 쓰인다

간단하면서도 강력하다

파이썬 if문은 꼭 내용에 뭔가가 하나라도 적혀 있어야 합니다
파이썬 if문 안에 내용을 적을땐 꼭 탭 한번 쳐주고 써야해요
(들여쓰기 필수)
"""

if(True):
    #print(f"조건문이 True 라서 여기가 실행 됬네요")
    # pass는 아무 의미 없는 코드
    pass
if False:
    print(f"조건문이 False라서 여기는 실행 안됬네요")

a= "      "
if(a):
    #print(f"a : {a}")
    None
a= ""
if(0):
    #print(f"0 : {0}")
    None


"""
if 문의 조건을 잘 써줘야 하는데,
이게 사람의 관점과 아주아주 틀리다
조건문은 컴퓨터 입장의 수식을 써줘야 한다
만약, 조건수식이 잘못되면, 빨간줄이 뜬다

컴퓨터 입장에선, 
None, null, "", 0, False
얘네들은 False와 동일하다

if 빨간문 보이면 자동으로 열어줘:
    pass
이런건 컴퓨터 입장에선 수식이 아님.

수식=
변수, 상수, 함수, 논리연산

"""

# 조건문에 변수 써보기
x=10
x="문자열"
x=[1,23]
x={"key1":"뭐뭐뭐"}
x=0.0000000001
if x:
    #print(f"x:{x}")
    None

# 상수
if 1:
    #print(f"조건문 실행")
    pass
if "문자열":
    #print(f"조건문 실행")
    pass
if [1,2,3]:
    #print(f"조건문 실행")
    pass


def dummyFunc():
    return True

if dummyFunc():
    #print(f"함수도 조건수식으로 쓸수 있네요. {dummyFunc()}")
    pass

a=3
b=2
if a>b:
    pass
if a==b:
    pass
if a<b:
    pass

"""
else if
위쪽 if가 참이 아니면 실행

else
조건이 다 참이 아니면 실행

elif든지, else든지 단독으로는 절대 사용 불가
if a:
    pass
elif a:
    pass
else :
    pass
"""
a=True
b=False
c=False
if b:
    #print(f" if 문")
    pass
elif c:
    #print(f"elif 문")
    pass
else :
    #print(f"else 문")
    pass

if a:
    pass
elif a:
    pass

"""
elif, else 는 꼭 쓰지 않아도 되요
"""

if a:
    if b:
        pass
elif b:
    if a:
        pass
    pass
    pass
my_typing=0
#my_typing=input("숫자를 입력하세요:")
print(f"my_typing: {my_typing}")
print(f"my_typing type: {type(my_typing)}")
my_number=int(my_typing)

"""
짝수/홀수 판별기

키보드로부터 숫자를 입력받고, 해당 숫자가
홀수인지 짝수인지 판별해서 알려주세요
 6 % 2 == 0    이러면 짝수
"""
my_typing=0
# my_typing=int(input("숫자를 입력하세요:"))

if my_typing % 2 == 0:
    print(f"짝수 입니다")
    pass
if my_typing % 2 !=0:
    print(f"홀수 입니다")

if my_typing % 2 == 0:
    print(f"짝수 입니다")
    pass
elif my_typing % 2 > 0:
    print(f"홀수 입니다")

if my_typing % 2 == 0:
    print(f"짝수 입니다")
    pass
else:
    print(f"홀수 입니다")


"""
성적 표시.
키보드로부터 숫자를 입력받고
90점 이상이면 A
89~80 이면 B
79~70 이면 C
69~60 이면 D
그 이하면 F

위에께 너무 쉬우면 계산기 만들어 보죠
"""
score=0
#score = int(input("성적점수 입력:"))
if score >= 90:
    print("A학점")
if 89 >= score >= 80:
    print("B학점")
if 79 >= score >= 70:
    print("C학점")
if 69>=score>=60 :
    print("D학점")
if score < 60:
    print("F학점")



person1={"이름":"박종진","비번":"1234"}
password=input("비밀번호:")

if password == person1['비번']:
    print("로그인 성공")
else:
    print("비밀번호가 틀렸습니다")

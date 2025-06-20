"""
https://wildojisan.tistory.com/12
-변수 개념, 변수 서언하기, 값 바꾸기, 컴퓨터 이론적으로 설명

안녕하세요. 2일차에도 만나서 반갑습니다.

컴퓨터 기본 :
얘는 맨 처음엔 계산기로 나왔어요.
그러다가 여러가지 기능들이 붙었어요.
컴퓨터의 기본 기능은 산술연산, 제어문, 반복문

요런것들을 조합해서 일을 시킴

그래서, 우리가 상상 하는거만큼, 대단한 일을 하진 못함.
얘가 가진 장점은 무식하게 빠른 산술연산
???
챗 지피티는 뭔데...

얘도 사람이 알아듣는 문자나 이미지 같은것을 숫자로 어거지로 
끼워 맞춰서 연산 때리게 하고
컴퓨터의 숫자를 어거지로 사람이 알아듣는 방법으로 변환 시킨거다

오늘은 컴퓨터 프로그래밍에서 모든분야 공통으로 쓰이는 변수에 대해 알아보겠습니다.
수학에선 변하는 숫자 = x
그냥 수학개념에서 좀더 뭘 얻었어요

쉽게 얘기하면 박스
어렵게 얘기하면 메모리 공간 입니다
여기에 데이터를 담는게 변수입니다

컴퓨터 주요 부품
CPU - 메인 계산기
GPU - 특별한 계산기
메모리 - 아주 중요. 사람으로 치면 주머니
하드디스크 - 얘는 창고

변수는 데이터를 메모리에 저장 시키는 방법입니다.
"""
"""
수학에선 x 는 10이다
프로그래밍 언어에선, x 라는 박스에 10을 담았다
""" 
# x 라는 변수가 처음 등장. 이건 x 라는 변수를 선언한거에요
x=10 
# x 라는 변수가 예전에 등장 했고, 또 등장 했으니, 이번에는
# x 라는 박스의 내용물을 바꾼거에요
x=2
"""
코딩 하다가 밑에 빨간줄 같은게 생기면, 문법 에러가 있다는 뜻입니다
Statements must be separated by newlines or semicolons
문장은 새로운 줄이나 세미콜론(;) 로 나눠야되요

빨간줄 에러가 뜨면, 마우스 올려서 에러메세지는 보지만,
정확한 이유를 안 알려주면, 경험으로 해결해야 한다
"""

"""
변수 명명 규칙
1. 띄어쓰지 금지
my car = "밴츠"

2. 예약어 금지
def, int, string, bool
요렇게 파이썬 만든 사람이 이미 만든 변수?는 변수로 쓸수 없어요
string="문자" X
mystring="문자" O

3. 특수기호 금지
특수 기호들은 산술연산 용도로 쓰임.
변수이름에 이런걸 섞으면, 컴퓨터가 바보됨
*mycar
%mycar
$mar

4. 숫자로 시작하면 안됨
1st
2nd

변수이름 지을때 권장사항은, 
영어로 되어있고, 숫자는 중간이나 끝에 있는거
"""
# 
"""
변수 만들기 name 이라는 변수를 만들고, 내 이름을 초기값으로 정해보기
name 이라는 변수를 ""(빈 문자열로 값을 바꿔보기)  
"""
x=10

name="박종진";
print(f"name : {name}")
name = ""
print(f"name : {name}")

x=True

1+2 # 3 
print(f"1+2 : {1+2}")
"hjghgy"

"""
새로운 변수가 등장할 때마다, 계속 메모리에 쌓인다
그러면... 변수가 한도끝도없이 계속 만들어지면 어떻게될까???

c, c++ 사람이 직접 제거명령을 해줘야되요
그외... 파이썬은  복불복입니다????
변수가 123232 종류가 있어요
파이썬이 판단해서 엣날꺼 안쓰는거 같은데??? 하면 옛날꺼 버리고
다 사용하는거 같은데?? 하면 다ㅣ 가지고 가요
그러다가, 더 뿔어나면 터짐
"""

"""
기본 자료형:
사람 기준에서 그나마 제일 쉬운거
x= 10       정수
x= 1.1      실수
x= ""       문자열
x= True     Bool대수
x= {"키":"값"} dictionary
x= [1,2,3]  list

x=numpy
x=tensor
"""

"""
1.변수 x 만들고 초기값 1로 해주기
2.변수 y 만들고 초기값 2로 해주기
3.변수 z를 만들고 x+y 한 값을 담아주기
"""
x=1
y=2
z=x+y
print(f"z: {z}")















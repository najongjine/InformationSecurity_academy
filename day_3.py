"""
자바 특강

파이썬:
a=10
if
a="dfdd"
switch
a=True

=?a={"key1":"value1"}

답은? 

prinf("%d")

for
[a,b]=[b,c]

a[::2]


자바:
int a=10;
String b="dd";
Boolean c=true
float d=1.1

나머지는 다 클래스

sysout(a+b+c+d)

if(){
}
for(int i=0; i<10; i++){
}
switch(){
}
while()

do{
dfdfddd 무조건 한번 실행
}
while(){
조건 만족할때만 진입
}

상속
추상화
인터페이스
생성자
static
this
overriding
overloading

c 랑 파이썬은

함수 문제 아닌이상, 무조건 위에서 아래로

자바 문제는 절대 그렇게 안나옴

부모, 자식, 오버라이딩, 업케스팅 


class Parent{
    int a=0;
    Parent(){}
}
class Child extend Parent{
    int a=0;
    Child(){

    }
}
class void main(){
    Parent parent=new Parent();
    Child child=new Child();
    Parent child2=new Child();
}


c언어 에서 제일 어려운데
포인터 - 주소값이 뭔가요 !!!! xxxxxxxxxxxxxxxxx
int * a= "dfdfgsdfgdfgdf"
b=&a  a 랑 맵핑 했구나. 문법오류 생각 말기
prinf(%s, a)  & 붙여야 같 나오나? 그런거 고민 x 무조건 값 나옴

malloc 계산 필요 없음
왜냐면, 무조건 정수로 떨어지는거 나올거임
int [] a={1,2,3}
int size= malloc(a/10%99)
"""


"""
https://wildojisan.tistory.com/12
-기본 자료형
"""
a=3
# a 라는 박스에 있는 값을 + 1 시키고
# 다시 a라는 박스에 담음
a=a+1 
a+=1

# 얘네들은, 계산은 했지만, 박스에는 안담음
a+1
1+2

# 정수
a = 10

# 실수(decimal)
a= 1.1

# 문자열
a="ddfd"
a="1+1"

# 논리형
a= True
a= False

# 배열
a = [1,2,3]
a= ["사과","바나나","망고"]

# 딕셔네리(Dictionary)
a= {"key1":"value1"}
a= {"key1":99}
a= {"key1":True}

# 튜플
a= (10,10,1)

"""
1. 99 라는 값을 가지는 num1 이라는 변수를 선언하세요
2. "멍멍이" 라는 str1 이라는 변수를 선언하세요
3. 기본값이 False인 boolvar 이라는 변수를 선언하세요
"""
num1=99
num1="99"
str1="멍멍이"
boolvar=False
boolvar="False"

num2=9
# print(f"type(num2):{type(num2)}")
num3="1"
# print(f"type(num3):{type(num3)}")
"""
TypeError(에러났다): 
unsupported(못함) operand(연산자) type(s) for +: 
'int' and 'str'   
이 뜻은 정수(int) 랑 문자열(str) 은 더하기 연산을 할수 없습니다
"""
#print(f"num2+num3={num2+num3}")

"""
컴퓨터에선 특수 문자 기호들이, 상황에 따라서
다른 연산을 하기도 합니다
예를들어서 문자열 + 문자열은 이어 붙이기라는 뜻입니다
"""
num2="9"
num3="1"
# print(f"num2+num3={num2+num3}")
# "91"

"""
파이썬 기본 자료형 중에서 리스트 라는 놈이 있다.
얘는 수학의 백터(선형대수) 가 아니다.
파이썬의 리스트는 서랍 같은 놈이다
+ 연산을 하면, 문자열처럼 붙이기를 한다
"""
list1=[1,2]
list2=[3,4]
list3= list1+list2
# print(f"list1+list2={list3}")

list1=["문자1","문자2"]
# 리스트에서 원소 접근   "문자1" 출력
#print(f"list1[0]={list1[0]}")

"""
IndexError(참조위치에러): 
list index(참조위치) out of range(범위를 벗어남)
"""
# print(f"list1[2]:{list1[2]}")

bool1=True
bool2=False

# 1
# print(f"bool+bool2={bool1+bool2}")

dict1={"제품명":"바나나"}
dict2={"제품명":"딸기"}
# 에러남. 딕셔네리는 연산을 할수 없다고 함
# print(f"dict1+dict2={dict1+dict2}")


"""
리스트는 여러가지를 한꺼번에 담을수 있는놈
파이썬 리스트는 아무거나 다 담을수 있음
나중에 배울 numpy 와 리스트는 다른놈임
"""
#      0   1  2  3
list1=[99,80,60,70]
list2=["고양이","개","말"]

"""
리스트
list1=[99,80,60,70]
에서 첫번째 원소와 마지막 원소를 더해서 출력해 보세요
"""

#      0   1  2  3  4
#     -5 -4  -3 -2 -1
list1=[99,80,60,70,5]
"""
정보처리 보실분 참조용
리스트 인덱스-
list1[-1] == list1[4] # 5
list1[-2] == list1[3] # 70

리스트 슬라이싱- 
list1[1:3] == [80, 60] # 인덱스 1~ 인덱스 2
list1[:3] == [99, 80, 60] # 인덱스 0~2
list1[-4:-2] == [80, 60] # 거꾸로 가야함.

start = 2 → 인덱스 2부터 시작
step = -1 → 거꾸로 이동
stop = 0 → 0번째 전까지. 0 인덱스는 포함하지 않는다. 즉 1에서 멈춤
list1[2:0:-1] == [60, 80]


#      0   1  2  3  4
#     -5 -4  -3 -2 -1
list1=[99,80,60,70,5]

시작은 1번째, 마지막은 4번째. 스태핑이 2니깐, 하나 껑충 뜀
list1[1:5:2] == [80, 70]

"""
# print(list1[1:5:])

"""
딕셔네리-
서버에서 웹으로 데이터 전달할때 많이 쓰이는 자료형
          key    값
person1={"이름":"뭐뭐1","학번":"11121"}
"""
person1={"이름":"뭐뭐1","학번":"11121"}
print(f"person1:{person1}")

coupang_item1={"name":"컴퓨터","price":"233423원"
               ,"제조사":"삼성"}
coupang_item2={"name":"옥수수","price":"2334원","제조사":"농장"}
coupang_item3={"name":"샴푸","price":"1334원","제조사":"화장품회사"}

#               0               1            2
coupang_list=[coupang_item1,coupang_item2,coupang_item3]

"""
coupang_list 1번째 인덱스의 제품 이름과 제조사 정보를 printf 로
출력해 보세요
"""
print(f"coupang_list[1]: {coupang_list[1]['name']},{coupang_list[1]['제조사']}")

coupang_item1={"name":"컴퓨터","price":"233423원"
               ,"제조사":"삼성", 
               "sub":{"name":"cpu","model":"ryzen5600"}
               }
coupang_item1['sub']['model']
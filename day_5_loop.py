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
    print(e)
    pass
"""
시험문제 낼때 빼고는 잘 안써요.
왜냐면, 조건을 잘못 쓰면, 계속 True 상태가 되서
무한루프에 빠져요
"""
i=0
while i<3:
    #print(i)
    #i=i+1, ++i, i++, i+=1
    pass
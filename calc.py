expression = input("계산할 수식을 입력하세요: ")

try:
    result = eval(expression)
    print("결과:", result)
except:
    print("잘못된 수식입니다.")
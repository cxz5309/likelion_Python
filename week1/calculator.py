# 실습1 파이썬 계산기 만들기

# 프로그램 시나리오
# 1. 사용자에게 프로그램 설명을 한다. 사용방법 등
# 2. 기능을 입력 받는다.
# 3. 기능과 계산할 값을 입력 받는다.
# 4. 계산 한 결과값을 출력한다.

while True:
    menu = input("""1. 더하기
2. 빼기
3. 곱하기
4. 나누기
5. 계산기 종료
""")
    if menu in ['5', 'q', 'Q']:
        break
    num1 = int(input("숫자1 : "))
    num2 = int(input("숫자2 : "))
    if menu == '1':
        print(num1+num2)
    elif menu == '2':
        print(num1-num2)
    elif menu == '3':
        print(num1*num2)
    elif menu == '4':
        print(num1/num2)

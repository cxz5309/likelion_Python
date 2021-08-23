money = input()
menuNum = input('''1. 아아
2. 따아
3. 라떼''')
myDic = {1: ['아아', 1000], 2: ['따아', 2000], 3: ['라떼', 3000]}
print(f'{myDic[menuNum][0]}입니다! 거스름돈 {money - myDic[menuNum][1]}')

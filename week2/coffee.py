myDic = {
    1: {'name': '아아', 'price': 1000, '': 1},
    2: {'name': '따아', 'price': 2000, '': 2},
    3: {'name': '라떼', 'price': 3000, '': 3},
}

while(True):
    money = int(input('준 돈 : '))
    menuNum = int(input('''1. 아아
2. 따아
3. 라떼
주문 번호 : '''))
    count = int(input('수량 : '))

    if(myDic[menuNum]['stock'] - count >= 0):
        print('{0} 주문! 거스름돈은 {1}원 입니다'
              .format(myDic[menuNum]['name'], str(money - myDic[menuNum]['price'])))

        myDic[menuNum]['stock'] -= count
        print('{0} 개 남아있습니다'.format(myDic[menuNum]['stock']))

    else:
        print('주문불가!')

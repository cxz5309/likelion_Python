
while True:
    a = input('단 : ')
    if a in ['q', 'Q']:
        break
    for i in range(1, 10):
        print(f'{int(a)} X {i} = {int(a) * i}')
    b = input('곱 : ')
    print(f'{int(a)} X {int(b)} = {int(a) * int(b)}')

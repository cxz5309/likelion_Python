a = int(input()) + 1
cnt = 0
for i in range(1, a):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        cnt = cnt + 1
        print('*', end='' if i == a-1 else ',')
    elif i == a-1:
        print(i, end=' ')
    else:
        print(i, end=',')
    if i % 10 == 0:
        print()
print()
print('cnt : ', cnt)

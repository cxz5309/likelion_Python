num = 1
text = '1'
print(type(num))
print(type(text))
print(type(num) == type(text))

user_name = 'young'
print(user_name)

floatNum = 3.14
print(type(floatNum))

typeBool = True
print(f'{typeBool}={type(typeBool)}')

list_num = [1, 2, 3, 4]
print(list_num)
print(list_num[3])

dict_item = {'name': 'young'}
print(dict_item)
print(dict_item['name'])
print(dict_item.get('name'))

title = '멋직 서울 6기'
print(title[:2])

# f = open('./test/fileStream.txt', mode='wt', encoding='utf-8')
# f.write('파이썬으로 파일을 작성하고 있습니다.')
# f.write('newline 문자로 개행해봅니다.\n')
# f.write('개행이 잘되었나요?')
# f.close()

r = open('./test/fileStream.txt', mode='rt', encoding='utf-8')
print(r.readlines())
r.close()

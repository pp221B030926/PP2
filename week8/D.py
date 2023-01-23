import re
txt = open('1.txt', mode = 'r')
a = txt.read()
b = re.findall(r'(@.+(-))', a)
c = '''Добрый вечер/Добрый день, Извиняюсь если отвлекаю вас, но нашел ваш канал '''
d = ''' в телеметре, и хочу предложить вам услуги по ведению контента в вашем канале, в том случае если у вас нету контент менеджера'''
e = '''Вот тут сможете посмотреть с кем работаем: https://t.me/ELLAGENCY
Если есть вопросы, спрашивайте ☺️'''
# print(b)
for i in b:
    ans = i[0].replace('-','')
    print(c, end = '')
    print(ans, end = '')
    print(d)
    print('')
    print(e)
    print('')
    print('')
# print(' '.join([j for j in b]), end = '')
txt.close()
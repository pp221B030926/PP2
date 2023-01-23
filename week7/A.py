import re
txt = open('input.txt', mode = 'r')
a = txt.read()
stan = re.findall(r'(\w+)stan', a)
b = re.findall(r'\d+', a)
c = re.findall(r'  (.+)', a)
# c = re.findall(r'(.+)', a)
print("Countries whose names end with 'stan':")
print('stan, '.join([j for j in stan]), end = '')
print('stan')
txt.close()
txt = open('input.txt', mode = 'r')
d = txt.readlines()
cnt = 0
f = []
for i in c:
    e = []
    sum = ''
    for j in i:
        sum += j
        if j == ' ':
            e.append(sum)
            sum = ''
    e.append(sum)
    f.append(e)
g = []
for i in f:
    if(len(i[len(i) - 1]) >= 3):
        g.append(i)
    elif(int(i[len(i) - 1]) >= 50):
        g.append(i)
h = []
for i in g:
    sum = ''
    for j in i[len(i) - 5]:
        if j >= '0' and j <= '9':
            sum += j
    if int(sum) >= 5000000:
        h.append(i)
for i in h:
    for j in range(0, len(i) - 5):
        print(i[j], end = ' ')
    print('')
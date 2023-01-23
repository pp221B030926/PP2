import re
d = dict()
v = []
s = []
txt = open('txt.txt', mode = 'r', encoding = 'utf_8')
a = txt.read()
b1 = re.findall(r'\((.+)\/', a)
b2 = re.findall(r'\/(.+),', a)
c = re.findall(r',(.+)\)', a)
e = re.findall(r'(.+) \(', a)
cnt = 0
b3 = []
for i in b1:
    sum = float(int(b1[cnt]) / int(b2[cnt]))
    cnt += 1
    b3.append(sum)
b = sorted(b3)
txt.close()
txt = open('txt.txt', mode = 'r', encoding = 'utf_8')
f = txt.readlines()
cnt = 0
for i in e:
    d[i] = b3[cnt]
    v.append((i,int(c[cnt])))
    cnt += 1
for key, value in sorted(d.items(), key = lambda item: item[1], reverse = True):
    s.append((key,value))
for j in sorted(v, key = lambda v:v[1],reverse = True):
    print(j)
    


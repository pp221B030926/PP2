n = int(input())
d = dict()
v = dict()
e = dict()
a = 97
for i in range(26):
    d[chr(a)] = 0
    a += 1
a = 65
for i in range(26):
    v[chr(a)] = 0
    a += 1
a = 48
for i in range(10):
    e[chr(a)] = 0
    a += 1
for i in range(n):
    l = str(input())
    for j in l:
        # print(type(ord(j)))
        for key,value in d.items():
            if ord(key) == ord(j):
                value = 1
                break
        for key,value in v.items():
            if ord(key) == ord(j):
                value = 1
                break
        for key,value in e.items():
            if ord(key) == ord(j):
                value = 1
                break
print("Lower case:", end = ' ')
for key, value in d.items():
    if value == 0:
        print(key, end = ' ')
print(' ')
print("Upper case:", end = ' ')
for key, value in v.items():
    if value == 0:
        print(key, end = ' ')
print(' ')
print("Numbers:", end = ' ')
for key, value in e.items():
    if value == 0:
        print(key, end = ' ')
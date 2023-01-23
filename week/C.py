import math
a = str(input())
c = ''
cnt = 0
sum = 0
e = len(a)
while e > 0:
    d = int(a[cnt]) * 8
    cnt = cnt + 1
    sum = sum + d
    e = e - 1
print(sum)
a = list(map(int, input().split()))
cnt = 0
a.sort()
c = len(a)
cnt = 0
for x in a:
    if int(x) > 0:
        break
    cnt = cnt + 1
sum = 1
d = c - cnt
e = 0
while d > 0:
    if(a[cnt] != sum):
        print(sum)
        e = e + 1
        break
    cnt = cnt + 1
    sum = sum + 1
    d = d - 1
if e == 0:
    print(sum) 
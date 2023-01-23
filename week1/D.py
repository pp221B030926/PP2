n = int(input())
d = dict()
sum1 = 0
sum2 = 0
sum3 = 0
for i in range(n):
    l = input().split()
    if l[2] not in d.keys():
        d[l[2]] = int(l[3])
    else: 
        d[l[2]] += int(l[3])
    if int(l[2]) == 9:
        sum1 += 1
    if int(l[2]) == 10:
        sum2 += 1
    if int(l[2]) == 11:
        sum3 += 1
arr = []
arr.append(sum1)
arr.append(sum2)
arr.append(sum3)
a = 0
for i in sorted(d.keys(), key = int):
    for j in d.values():
        if d[i] == j:
            e = float(j / arr[a])
            a += 1
            print(e, end = ' ')

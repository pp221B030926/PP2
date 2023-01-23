n = int(input())
d = dict()
s = set()
for i in range(n):
    l = str(input())
    if l not in d:
        d[l] = 1
    else:
        d[l] += 1
sum = 0
for i in sorted(d.values(), reverse = True):
    for j in d.keys():
        if d[j] == i:
            if i > float(n / 2):
                print(j)
                exit()
    for j in d.keys():
        if d[j] == i:
            print(j)
            sum += 1
            if sum == 2:
                exit()
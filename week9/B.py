import itertools
a = str(input())
b = list(itertools.permutations(a))
for i in b:
    ans = ''
    for j in i:
        ans += j
    if int(ans) % 30 == 0:
        print('YES')
        exit()
print('NO')
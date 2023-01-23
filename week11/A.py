a = int(input())
ans = ''
d = []
def check(sum):
    c = 1
    while c <= sum:
        c *= 2
    if c == sum:
        return 1
    else: return 2
for i in range(a):
    b = input()
    sum = 0
    for j in b:
        cnt = 0
        ok = True
        while ok == True:
            print(cnt)
            if (j[cnt] >= 'A' and j[cnt] <= 'Z'):
                sum += 1
            if j[cnt] >= 'a' and j[cnt] <= 'z':
                sum += 1
            if (ord(j[cnt]) >= 32 and ord(j[cnt]) <= 64) or cnt == len(j) - 1:
                # print(sum)
                if check(sum) == 1:
                    ans += 'H '
                else: 
                    ans += 'C '
                ok = False
            cnt += 1
        sum = 0 
    ans += '\n'
print(ans)
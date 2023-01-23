n = int(input())
ans = ''
sum = 0
for i in range(n):
    l = str(input())
    # print(type(l[0]))
    if sum == 0:
        a = chr(ord(l[0]) - 32)
        m = '' + a
        sum += 1
        while sum < len(l):
            m += l[sum]
            sum += 1
        ans += str(m)
        continue
    ans += ' ' + str(l)
ans += '.'
print(ans)
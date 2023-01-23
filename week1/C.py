n = int(input())
max = 0
sum = 1
for i in range(n):
    l = input().split()
    if max < int(l[3]):
        max = int(l[3])
        ans = l[0] + ' ' + l[1]
        continue
    if max == int(l[3]):
        sum += 1
if sum > 1:
    print(sum)
if sum == 1:
    print(ans)

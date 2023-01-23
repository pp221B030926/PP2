import re
a = str(input())
cnt = re.findall(r'192',a)
cnt1 = re.findall(r'0,', a)
cnt2 = re.findall(r'0%', a)
cnt3 = re.findall(r'75%', a)
sum = 0
if len(cnt) == 3:
    print('YES')
    sum += 1
if len(cnt1) == 1 and len(cnt2) == 1 and len(cnt3) == 1:
    print('YES')
    sum += 1
if sum == 0:
    print('NO')
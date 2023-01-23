import re
a = str(input())
if len(a) == 16:
    year = re.findall(r'(.+)\/..\/', a)
    month = re.findall(r'\/(.+)\/', a)
    day = re.findall(r'\/..\/(.+) ', a)
    hour = re.findall(r' (.+):', a)
    minute = re.findall(r':(.+)', a)
    sum = 0
    if int(year[0]) >= 1000 and int(year[0]) <= 2012 and int(month[0]) >= 1 and int(month[0]) <= 12:
        print('Yes')
        sum += 1
    if sum == 0:
        print('No')
if len(a) != 16:
    print('No')
# print(month)
# print(day)
# print(hour)
# print(minute)
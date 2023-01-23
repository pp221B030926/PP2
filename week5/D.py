import re 
a = str(input())
sum = 0
https = re.findall('https://......',a)
if len(https) == 1:
    print('Yes')
    sum += 1
http = re.findall('http://......',a)
if len(http) == 1:
    print('Yes')
    sum += 1
if sum == 0:
    print('No')
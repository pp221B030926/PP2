import re
a = str(input())
b = re.sub('^a', '!', a)
c = re.sub(' a', ' !', a)
d = re.sub('(!\w+)', '(!\w+)!',a)
print(d)
a = input().split()
b = str(input())
c = ''
for x in a:
    c = c + x + ' '
d = c.replace(b,'')
print(d)
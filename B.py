a = str(input())
s = 0
for i in a:
    s += ord(i)
if s % 2 == 0:
    print('even')
if s % 2 == 1:
    print('odd')
a = input().split()
d = dict()
v = dict()
c = dict()
for i in a:
    if i not in d.keys():
        d[i] = 1
        print(i, end = ' ')
    else: 
        d[i] += 1
        ans = '**' + i + '**'
        print(ans, end = ' ')
# for keys, values in d.items():
#     if values == 1:
#         print(keys, end = ' ')
#     if values > 1:
#         if keys not in v.keys():
#             print(keys, end = ' ')
#             v[keys] = 1
#         for key in v.keys():
#             if key == keys:
#                 ans = '**' + key + '**'
#                 print(ans, end = ' ')
#                 break
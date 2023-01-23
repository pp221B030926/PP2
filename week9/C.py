a = int(input())
c = [1,5,10,20,50,100,200,500,1000,2000]
s = []
for i in range(a):
    b = input().split()
    cnt = 0
    sum = 0
    ans = 0
    for j in range(1, len(b)):
        d = int(b[j])
        while d > 0:
            sum += c[cnt]
            ans += 1
            if sum == int(b[0]):
                break
            if sum > int(b[0]):
                e = sum - int(b[0])
                k = j - 1
                cnt -= 1
                q = 1
                while q >= 1:
                    l = int(b[k])
                    while l > 0:
                        e -= c[cnt]
                        sum -= c[cnt]
                        if e < 0:
                            e += c[cnt]
                            sum += c[cnt]
                            k -= 1
                            break
                        if e == 0:
                            ans -= 1
                            q = 0
                            break
                        if e > 0:
                            ans -= 1
                        if l == 0:
                            break
                        l -= 1
                    k -= 1
                    cnt -= 1
                break
            d -= 1
        if sum == int(b[0]):
            break
        cnt += 1
    if sum >= int(b[0]):
        s.append(ans)
    if sum < int(b[0]):
        s.append(-1)
for i in s:
    print(i)
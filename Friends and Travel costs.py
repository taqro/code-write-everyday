n, k = map(int,input().split())

AB = []
for i in range(n):
    a, b = map(int,input().split())
    AB.append([a,b])

AB.sort()

ans = k
for i in range(n):
    if ans < AB[i][0]:
        break
    else:
        ans += AB[i][1]

print(ans)

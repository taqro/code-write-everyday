n, k = map(int,input().split())

C = list(map(int, input().split()))

color = {}

for i in range(n):
    color.setdefault(C[i], 0)

tmp = 0
for i in range(k):
    if color[C[i]] == 0:
        tmp += 1
    color[C[i]] += 1

ans = tmp
for i in range(n-k):
    if color[C[i]] == 1:
        tmp -= 1
    color[C[i]] -= 1
    if color[C[i+k]] == 0:
        tmp += 1
    color[C[i+k]] += 1
    ans = max(ans, tmp)

print(ans)

N = int(input())
P = list(map(int, input().split()))

min = 10 ** 9
ans = 0
for i in range(N):
  if min >= P[i]:
    min = P[i]
    ans += 1

print(ans)

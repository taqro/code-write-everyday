N = int(input())
W = list(map(int, input().split()))

ans = 10 ** 9
for i in range(1, N):
  s_1 = 0
  s_2 = 0
  for j in range(i):
    s_1 += W[j]
  for k in range(i, N):
    s_2 += W[k]
  if ans > abs(s_2 - s_1):
    ans = abs(s_2 - s_1)

print(ans)

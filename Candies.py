N = int(input())

s = [[] * N] * 2

for i in range(2):
  s[i] = list(map(int, input().split()))

ans = 0

for i in range(N):
  sum = 0
  for j in range(i + 1):
    sum += s[0][j]
  for j in range(i, N):
    sum += s[1][j]
  if ans <= sum:
    ans = sum

print(ans)

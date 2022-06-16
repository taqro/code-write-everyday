N = int(input())
X = list(map(int, input().split()))

ans = 10 ** 9

for i in range(300 + 1):
  sum = 0
  for j in range(N):
    if X[j] == i:
      continue
    else:
      sum += (X[j] - i) ** 2
  if ans > sum:
    ans = sum

print(ans)

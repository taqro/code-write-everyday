K, S = map(int, input().split())

ans = 0
for i in range(K + 1):
  for j in range(K + 1):
    if S - (i + j) <= K and 0 <= S - (i + j):
      ans += 1

print(ans)

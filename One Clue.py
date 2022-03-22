K, X = map(int, input().split())

ans = []

for i in range(X - (K - 1), X + (K - 1) + 1):
  ans.append(str(i))

print(" ".join(ans))

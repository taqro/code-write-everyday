A, B, K = map(int, input().split())

ans = 0
for i in range(100):
  if A * (K ** i) >= B:
    print(i)
    break

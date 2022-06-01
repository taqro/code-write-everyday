N = int(input())

ans = 0

for i in range(1, N):
  for j in range(i, (N // i) + 1):
    if N - i * j > 0:
      if i != j:
        ans += 2
      else:
        ans += 1

print(ans)

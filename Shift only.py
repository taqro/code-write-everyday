N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(1000):
  cnt = 0
  for j in range(N):
    if A[j] % 2 == 0:
      A[j] /= 2
      cnt += 1
    else:
      break
  if cnt == N:
    ans += 1
  else:
    break

print(ans)

N = int(input())
A = list(map(int, input().split()))
A.insert(0,0)

ans = [0] * N
for i in range(2, N + 1):
  ans[A[i - 1] - 1] += 1

for i in range(N):
  print(ans[i])

N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = [0] * (N + 1)
next_index = X
ans[next_index] += 1
for i in range(N):
  ans[A[next_index - 1]] += 1
  next_index = A[next_index - 1]

print(N + 1 - ans.count(0))

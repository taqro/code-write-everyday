N, S, T = map(int, input().split())
W = int(input())
A = []
ans = 0
for i in range(N - 1):
  A.append(int(input()))

if S <= W and W <= T:
  ans += 1

for i in range(N - 1):
  if S <= W + A[i] and W + A[i] <= T:
    ans += 1
  W += A[i]

print(ans)

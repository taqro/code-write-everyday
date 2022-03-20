N, K = map(int, input().split())
d = [0] * K
A = [[]] * K

for i in range(K):
  d[i] = int(input())
  A[i] = list(map(int, input().split()))

cnt = [0] * 100

for i in range(K):
  for j in range(len(A[i])):
    cnt[A[i][j] - 1] += 1

ans = 0
for i in cnt[0:N]:
  if i == 0:
    ans += 1

print(ans)

H, W = map(int, input().split())

A = [0] * H
for i in range(H):
  A[i] = list(map(int, input().split()))

arr = [0] * 101

for i in range(H):
  for j in range(W):
    arr[A[i][j]] += 1

min_index = 0
for i in range(101):
  if arr[i] != 0:
    min_index = i
    break

ans = 0
for i in range(min_index, 101):
  ans += arr[i] * (i - min_index)

print(ans)


N = int(input())
t = [0] * N
for i in range(N):
  t[i] = int(input())

min = 10 * 9

for i in range(1 << N):
  right = 0
  left = 0
  for j in range(N):
    if (i >> j) & 1:
      left += t[j]
    else:
      right += t[j]
  if min > max(left, right):
    min = max(left, right)

print(min)

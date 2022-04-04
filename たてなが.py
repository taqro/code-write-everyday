H, W = map(int, input().split())
C = [[]] * H
for i in range(H):
  C[i] = list(input())

ans = [[""] * W] * (2 * H)
index = 0
for i in range(H):
  ans[index] = C[i]
  index += 1
  ans[index] = C[i]
  index += 1

for i in range(2 * H):
  print("".join(ans[i]))

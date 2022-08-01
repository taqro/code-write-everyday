H, W = map(int, input().split())
S = [[]] * H
for i in range(H):
  S[i] = list(input())

x = []
y = []
for i in range(H):
  for j in range(W):
    if S[i][j] == "o":
      x.append(i)
      y.append(j)

ans = 10 ** 9
for i in range(len(x)):
  for j in range(i + 1, len(x)):
    dist = abs(x[i] - x[j]) + abs(y[i] - y[j])
    if dist < ans:
      ans = dist

print(ans)

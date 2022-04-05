H, W, X, Y = map(int, input().split())
S = [[]] * H
for i in range(H):
  S[i] = list(input())

ans = 0
for i in range(Y, W):
  if S[X - 1][i] == "#":
    break
  ans += 1

for i in range(Y - 1)[::-1]:
  if S[X - 1][i] == "#":
    break
  ans += 1

for i in range(X, H):
  if S[i][Y - 1] == "#":
    break
  ans += 1

for i in range(X - 1)[::-1]:
  if S[i][Y - 1] == "#":
    break
  ans += 1

print(ans + 1)

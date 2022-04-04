N = int(input())
s = [[]] * N
for i in range(N):
  s[i] = list(input())

ans = [[""] * N] * N
for i in range(N):
  for j in range(N):
    ans[i][j] = s[(N - 1) - j][i]
  print("".join(ans[i]))



H, W = map(int, input().split())

s = [[0] * W] * H

for i in range(H):
  s[i] = list(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = "Yes"
for i in range(H):
  for j in range(W):
    if s[i][j] == ".":
      continue
    if s[i][j] == "#":
      flag = 0
      for k in range(4):
        di = i + dy[k]
        dj = j + dx[k]
        if di < 0 or dj < 0 or di >= H or dj >= W  :
          continue
        if s[i][j] == s[di][dj]:
          flag = 1
      if flag == 0:
        ans = "No"

print(ans)


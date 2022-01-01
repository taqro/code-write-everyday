H, W = map(int, input().split())
s = [""] * H
for i in range(H):
  s[i] = list(input())

for i in range(H):
  for j in range(W):
    sum = 0
    if s[i][j] == ".":
      if i - 1 >= 0:
        if s[i - 1][j] == "#":
          sum += 1
      if i + 1 <= H - 1:
        if s[i + 1][j] == "#":
          sum += 1
      if j + 1 <= W - 1:
        if s[i][j + 1] == "#":
          sum += 1
      if j - 1 >= 0:
        if s[i][j - 1] == "#":
          sum += 1
      if i - 1 >= 0 and j + 1 <= W - 1:
        if s[i - 1][j + 1] == "#":
          sum += 1
      if i - 1 >= 0 and j - 1 >= 0:
        if s[i - 1][j - 1] == "#":
          sum += 1
      if i + 1 <= H - 1 and j + 1 <= W - 1:
        if s[i + 1][j + 1] == "#":
          sum += 1
      if i + 1 <= H - 1 and j - 1 >= 0:
        if s[i + 1][j - 1] == "#":
          sum += 1
      s[i][j] = str(sum)

a = ""
for i in range(H):
  for j in range(W):
    a += s[i][j]
  s[i] = a
  a = ""

for i in range(H):
  print(s[i])





c = [[]] * 4
for i in range(4):
  c[i] = list(input().split())

ans = [[""] * 4] * 4
for i in range(4):
  for j in range(i + 1, 4):
    c[i][j], c[abs(3 - i)][abs(3 - j)] = c[abs(3 - i)][abs(3 - j)], c[i][j]

c[0][0], c[3][3] = c[3][3], c[0][0]
c[1][1], c[2][2] = c[2][2], c[1][1]

for i in range(4):
  print(" ".join(c[i]))

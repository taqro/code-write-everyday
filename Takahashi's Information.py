c = [[] * 3] * 3
for i in range(3):
  c[i] = list(map(int, input().split()))

a = [0] * 3
b = [0] * 3

ans = "No"
for i in range(1000):
  a[0] = i
  b[0] = c[0][0] - a[0]
  b[1] = c[0][1] - a[0]
  b[2] = c[0][2] - a[0]
  a[1] = c[1][0] - b[0]
  a[2] = c[2][0] - b[0]

  if a[1] + b[1] == c[1][1] and a[1] + b[2] == c[1][2] and a[2] + b[1] == c[2][1] and a[2] + b[2] == c[2][2]:
    ans = "Yes"

print(ans)

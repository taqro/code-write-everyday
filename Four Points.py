x = [0] * 3
y = [0] * 3
for i in range(3):
  x[i], y[i] = map(int, input().split())

ans = [0] * 2

if x[0] == x[1]:
  ans[0] = x[2]
elif x[0] == x[2]:
  ans[0] = x[1]
else:
  ans[0] = x[0]

if y[0] == y[1]:
  ans[1] = y[2]
elif y[0] == y[2]:
  ans[1] = y[1]
else:
  ans[1] = y[0]

print(ans[0], ans[1])

W, H ,N = map(int, input().split())

x = [0] * N
y = [0] * N
a = [0] * N

for i in range(N):
  x[i], y[i], a[i] = map(int, input().split())

x_1 = 0
x_2 = W
y_1 = 0
y_2 = H

for i in range(N):
  if a[i] == 1:
    x_1 = max(x_1, x[i])
  elif a[i] == 2:
    x_2  = min(x_2, x[i])
  elif a[i] == 3:
    y_1 = max(y_1, y[i])
  elif a[i] == 4:
    y_2 = min(y_2, y[i])

x_diff = max(0, (x_2 - x_1))
y_diff = max(0, (y_2 - y_1))

print(x_diff * y_diff)

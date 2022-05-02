N = int(input())
X = [0] * N
Y = [0] * N
for i in range(N):
  X[i], Y[i] = map(int, input().split())

def culc_area(x_1, y_1, x_2, y_2, x_3, y_3):
  area = ((x_2 - x_1) * (y_3 - y_1) - (x_3 - x_1) * (y_2 - y_1)) / 2
  return area

ans = 0
for i in range(N):
  for j in range(i + 1, N):
    for k in range(j + 1, N):
      if culc_area(X[i], Y[i], X[j], Y[j], X[k], Y[k]) != 0:
        ans += 1

print(ans)



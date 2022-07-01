N = int(input())
t = [0] * N
x = [0] * N
y = [0] * N
for i in range(N):
  t[i], x[i], y[i] = map(int, input().split())

now_t = 0
now_x = 0
now_y = 0

ans = "Yes"

for i in range(N):
  diff_time = t[i] -now_t
  diff_space = abs(x[i] - now_x) + abs(y[i] - now_y)

  if diff_space > diff_time:
    ans = "No"
    break
  elif (diff_space - diff_time) % 2 != 0:
    ans = "No"
    break

  now_t = t[i]
  now_x = x[i]
  now_y = y[i]

print(ans)

import math

N = int(input())
R = [0] * N
for i in range(N):
  R[i] = int(input())

R.sort(reverse=True)

ans = 0
flag = 1
for i in range(N):
  if flag == 1:
    ans += R[i] ** 2
    flag = 0
  elif flag == 0:
    ans -= R[i] ** 2
    flag = 1

print(ans * math.pi)

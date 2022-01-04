N = int(input())
S = list(input())

sum_w = [0] * (N + 1)
sum_e = [0] * (N + 1)
ans = [0] * N
for i in range(N):
  if S[i] == "W":
    a = 1
  else:
    a = 0
  sum_w[i + 1] = sum_w[i] + a

  if S[i] == "E":
    a = 1
  else:
    a = 0
  sum_e[i + 1] = sum_e[i] + a

for i in range(N):
  ans[i] = sum_w[i] + (sum_e[N] - sum_e[i + 1])

print(min(ans))

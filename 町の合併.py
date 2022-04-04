N = int(input())
S = [0] * N
P = [0] * N
for i in range(N):
  S[i], P[i] = input().split()

sum = 0
for i in range(N):
  sum += int(P[i])

ans = "atcoder"
for i in range(N):
  if int(P[i]) > sum // 2:
    ans = S[i]
    break

print(ans)

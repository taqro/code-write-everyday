N, K = map(int, input().split())
P = [[]] * N
for i in range(N):
  P[i] = list(map(int, input().split()))

sum = [0] * N
for i in range(N):
  sum[i] = P[i][0] + P[i][1] + P[i][2]

t = sorted(sum, reverse=True)[K - 1]

for i in range(N):
  if sum[i] + 300 >= t:
    print("Yes")
  else:
    print("No")

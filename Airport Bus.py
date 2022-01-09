N, C, K = map(int, input().split())
T = [0] * N
for i in range(N):
  T[i] = int(input())

T.sort()
cnt = C
min = 0
start_time = 0
for i in range(N):
  if T[i] - start_time > K or cnt == C:
    min += 1
    start_time = T[i]
    cnt = 1
  else:
    cnt += 1

print(min)

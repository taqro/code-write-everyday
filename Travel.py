import itertools

N, K = map(int, input().split())
T = [[]] * N
for i in range(N):
  T[i] = list(map(int, input().split()))

arr = [*range(2, N + 1)]

ptn = list(itertools.permutations(arr))
ans = 0

for p in ptn:
  sum = 0
  now = 0
  for i in p:
    sum += T[now][i - 1]
    now = i - 1
  sum += T[now][0]
  if sum == K:
    ans += 1

print(ans)




N, M = map(int, input().split())
L = [0] * M
R = [0] * M
for i in range(M):
  L[i], R[i] = map(int, input().split())

min_range = L[0]
max_range = R[0]
for i in range(1, M):
  min_range = max(min_range, L[i])
  max_range = min(max_range, R[i])

ans = 0
for i in range(1, N + 1):
  if min_range <= i and i <= max_range:
    ans += 1

print(ans)




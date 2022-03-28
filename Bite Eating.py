N, L = map(int, input().split())

min_abs = 10 ** 9
min_index = 0
for i in range(N):
  if min_abs > abs(L + i):
    min_abs = abs (L + i)
    min_index = i

ans = 0

for i in range(N):
  if i == min_index:
    continue
  ans += L + i

print(ans)


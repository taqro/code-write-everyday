N, A, B = map(int, input().split())

ans = 0

for i in range(1, N + 1):
  n = list(str(i))
  sum = 0
  for j in range(len(n)):
    sum += int(n[j])
  if A <= sum and sum <= B:
    ans += i

print(ans)

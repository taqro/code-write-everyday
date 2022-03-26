N = int(input())

ans = 0
for i in range(1, N + 1):
  if i < 10:
    ans += 1
  if 99 < i < 1000:
    ans += 1
  if 9999 < i < 100000:
    ans += 1

print(ans)

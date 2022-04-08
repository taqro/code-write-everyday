n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
  if a[i] % 2 == 0:
    a[i] -= 1
    ans += 1
  if a[i] == 5:
    ans += 2

print(ans)

N = int(input())
a = list(map(int,input().split()))

a.sort()

ans = 0
for i in range(N - 1):
  ans += a[i + 1] - a[i]

print(ans)

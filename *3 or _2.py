N = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(N):
  if a[i] % 2 == 0:
    cnt = 0
    for j in range(1,100):
      if a[i] % 2 != 0:
        break
      a[i] /= 2
      cnt += 1
    ans += cnt

print(ans)

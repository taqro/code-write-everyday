N = int(input())
A = list(map(int, input().split()))


ans = 0
cnt = [0] * (10 ** 5)
for i in range(N):
  mo = A[i] % 200
  ans += cnt[mo]
  cnt[mo] += 1

print(ans)

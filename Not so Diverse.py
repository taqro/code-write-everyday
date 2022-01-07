N, K = map(int, input().split())

a = list(map(int, input().split()))

ans = [0] * N
a_s = set(a)
for i in a:
  ans[i - 1] += 1

ans.sort(reverse=True)

sum = 0
for i in range(K, N):
  if ans[i] == 0:
    break
  sum += ans[i]


print(sum)

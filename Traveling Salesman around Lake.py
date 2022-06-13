K, N = map(int, input().split())
A = list(map(int, input().split()))

diff = [0] * N
for i in range(N - 1):
  diff[i] = A[i + 1] - A[i]

diff[N - 1] = A[0] + (K - A[N - 1])

diff.sort(reverse=True)

ans = sum(diff[1:])

print(ans)

N, K = map(int, input().split())
h = [0] * N
for i in range(N):
  h[i] = int(input())

h.sort()

ans = 10 ** 10
for i in range(N - (K - 1)):
  diff = h[i + K - 1] - h[i]
  if diff < ans:
    ans = diff

print(ans)

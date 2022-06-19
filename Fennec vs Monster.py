N, K = map(int, input().split())
H = list(map(int, input().split()))

H.sort(reverse=True)

ans = 0
if N > K:
  for i in range(N):
    if i < K:
      continue
    else:
      ans += H[i]

print(ans)

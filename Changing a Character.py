N, K = map(int, input().split())
S = list(input())

S[K - 1] = S[K - 1].lower()

ans = ""
for i in S:
  ans += i

print(ans)


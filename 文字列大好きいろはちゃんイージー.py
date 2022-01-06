N, L = map(int, input().split())

S = [""] * N
for i in range(N):
  S[i] = input()

S.sort()

ans = ""
for s in S:
  ans += s

print(ans)

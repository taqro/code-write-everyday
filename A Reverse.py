L, R = map(int, input().split())
S = list(input())

T = S[L - 1: R]

U = T[::-1]

ans = ""

for i in range(L - 1):
  ans += S[i]

for u in U:
  ans += u

for i in range(R,len(S)):
  ans += S[i]

print(ans)

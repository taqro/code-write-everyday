S  = list(input())
N = int(input())
l = [0] * N
r = [0] * N
for i in range(N):
  l[i], r[i] = map(int, input().split())

for i in range(N):
  S[l[i] - 1: r[i]] = S[l[i] - 1: r[i]][::-1]

print("".join(S))

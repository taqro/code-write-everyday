N = int(input())
S = [""] * N
for i in range(N):
  S[i] = input()

T = {}
for s in S:
  if s in T:
    T[s] += 1
  else:
    T[s] = 1

print(max(T, key = T.get))


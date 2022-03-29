N = int(input())
S = [""] * N
P = [""] * N
for i in range(N):
  S[i], P[i] = input().split()

ans = list(range(N + 1))

for k in range(10):
  for i in range(N):
    for j in range(N):
      q = [*ans]
      s = q.index(i + 1)
      t = q.index(j + 1)
      if S[i] < S[j] and s > t:
        ans[s], ans[t] = ans[t], ans[s]
      elif S[i] == S[j] and s > t and int(P[i]) >   int(P[j]):
        ans[s], ans[t] = ans[t], ans[s]

for i in range(1, N + 1):
  print(ans[i])


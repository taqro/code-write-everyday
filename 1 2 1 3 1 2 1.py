N = int (input())

S =[[]] * (N + 1)

S[1] = [1]

for i in range(2, N + 1):
  S[i] = S[i - 1] + [i] + S[i - 1]

print(*S[N])


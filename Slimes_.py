N = int(input())
S = list(input())

ans = [S[0]]

for i in range(1, N):
  if S[i] == S[i - 1]:
    continue
  ans.append(S[i])

print(len(ans))

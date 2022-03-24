S = list(input())

ans = 0
if len(S) % 2 == 0:
  for i in range(len(S) // 2):
    if S[i] != S[::-1][i]:
      ans += 1
elif len(S) % 2 != 0:
  for i in range((len(S) + 1) // 2):
    if S[i] != S[::-1][i]:
      ans += 1

print(ans)

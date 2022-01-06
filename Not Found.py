S = list(input())

S.sort()
for i in range(len(S)):
  S[i] = ord(S[i])

ans = "None"
for i in range(97, 123):
  if i in S:
    continue
  else:
    ans = chr(i)
    break

print(ans)

S = list(input())
T = list(input())

ans = "Yes"
a = ord(T[0]) - ord(S[0])
if a < 0:
  a += 26

for i in range(len(S)):
  b = ord(T[i]) - ord(S[i])
  if b < 0:
    b += 26
  if b != a:
    ans ="No"
    break

print(ans)

W = list(input())

boin = ["a", "i", "u", "e", "o"]

ans = ""

for i in range(len(W)):
  if W[i] in boin:
    continue
  else:
    ans += W[i]

print(ans)

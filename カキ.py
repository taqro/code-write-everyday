S = [""] * 12
for i in range(12):
  S[i] = input()

ans = 0
for i in range(12):
  if "r" in S[i]:
    ans += 1

print(ans)

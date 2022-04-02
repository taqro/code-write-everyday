S = list(input())

ans = "AC"
if S[0] != "A":
  ans = "WA"

if S[2:-1].count("C") != 1:
  ans = "WA"

for i in range(len(S)):
  if S[i] != "A" and S[i] != "C" and S[i].isupper():
    ans = "WA"
    break

print(ans)

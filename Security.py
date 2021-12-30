S = list(input())

ans = "Good"
if S[0] == S[1]:
  ans = "Bad"
if S[1] == S[2]:
  ans = "Bad"
if S[2] == S[3]:
  ans = "Bad"

print(ans)

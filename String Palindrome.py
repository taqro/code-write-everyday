S = list(input())

ans = "No"
if S == S[::-1] and S[0:(len(S) - 1) // 2] == S[0:(len(S) - 1) // 2][::-1] and S[(len(S) + 3) // 2 - 1: len(S)] == S[(len(S) + 3) // 2 - 1: len(S)][:: -1]:
  ans = "Yes"

print(ans)


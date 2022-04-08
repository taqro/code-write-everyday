S = list(input())
T = list(input())

a = ["a", "t" , "c", "o", "d", "e", "r", "@"]

ans = "You can win"
for i in range(len(S)):
  if S[i] == "@" and T[i] not in a:
    ans = "You will lose"
  elif T[i] == "@" and S[i] not in a:
    ans = "You will lose"
  elif S[i] != "@" and T[i] != "@" and S[i] != T[i]:
    ans = "You will lose"

print(ans)


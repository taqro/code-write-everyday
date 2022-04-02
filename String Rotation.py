S = list(input())
T = list(input())

ans = "No"
for i in range(len(S)):
  a = S.pop(0)
  S.append(a)
  if S == T:
    ans = "Yes"
    break

print(ans)

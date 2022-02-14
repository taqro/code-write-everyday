S = list(input())

ans =[]
for i in range(len(S)):
  if S[i] == "6":
    ans.insert(0, "9")
  elif S[i] == "9":
    ans.insert(0, "6")
  else:
    ans.insert(0, S[i])

ans = ''.join(ans)

print(ans)

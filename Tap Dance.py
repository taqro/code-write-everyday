S = list(input())

ans = "Yes"
for i in range(len(S)):
  if i % 2 == 0:
    if S[i] != "R" and S[i] != "U" and S[i] != "D":
      ans = "No"
      break

  elif i % 2 != 0:
    if S[i] != "L" and S[i] != "U" and S[i] != "D":
      ans = "No"
      break

print(ans)

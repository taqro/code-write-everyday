S = input()

ans = "Yes"

for i in range(1,len(S) - 1):
  if S[i] == "o":
    if S[i - 1] == "x" and S[i + 1] == "x":
      continue
    else:
      ans ="No"
      break
  if S[i] == "x":
    if S[i - 1] == "o":
      if S[i + 1] == "x":
        continue
      else:
        ans = "No"
        break
    elif S[i - 1] == "x":
      if S[i + 1] == "o":
        continue
      else:
        ans = "No"
        break

if len(S) == 2:
  if S[0] == "o" and S[1] == "o":
    ans = "No"

print(ans)

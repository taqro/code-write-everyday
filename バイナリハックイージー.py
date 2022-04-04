s = list(input())

ans = []
for i in range(len(s)):
  if s[i] == "0":
    ans.append("0")
  elif s[i] == "1":
    ans.append("1")
  elif s[i] == "B" and len(ans) != 0:
    ans.pop(-1)
  elif s[i] == "B" and len(ans) == 0:
    pass

print("".join(ans))

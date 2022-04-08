s = list(input())

ans = ""
cnt = 1
for i in range(len(s)):
  if i == len(s) - 1:
    if cnt != 1:
      ans += s[i - 1] + str(cnt)
      break
    else:
      ans += s[i] + str(cnt)
      break
  if s[i] == s[i + 1]:
    cnt += 1
  else:
    ans += s[i] + str(cnt)
    cnt = 1

print(ans)


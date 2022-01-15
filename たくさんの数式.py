S = input()

ans = 0
sign =[""] * (len(S) - 1)
for i in range(1 << (len(S) - 1)):
  sign =[""] * (len(S) - 1)
  for j in range(len(S) - 1):
    if ((i >> j) & 1):
      sign[j] = "+"

  num_str = ""
  k = 0
  while k < (len(S) - 1):
    if sign[k] == "":
      if k == (len(S) - 1) - 1:
        num_str += S[k] + S[k + 1]
        ans += int(num_str)
        break
      num_str += S[k]
      k += 1
    elif sign[k] == "+":
      if k == (len(S) - 1) - 1:
        num_str += S[k]
        ans += int(num_str) + int(S[k + 1])
        break
      num_str += S[k]
      ans += int(num_str)
      k += 1
      num_str = ""

  if len(S) == 1:
    ans = int(S)

print(ans)

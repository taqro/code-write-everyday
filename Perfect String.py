S = list(input())

L_flag = False
U_flag = False
ans = "No"
for i in range(len(S)):
  if S[i].islower():
    L_flag = True
  if S[i].isupper():
    U_flag = True

flag = False
set_S = set(S)
if len(S) == len(set_S):
  flag = True

if flag and L_flag and U_flag:
  ans = "Yes"

print(ans)

S = list(input())

ans = 0
for i in range(len(S)):
  S.pop(-1)
  if len(S) % 2 == 0:
    if S[0:len(S) // 2] == S[len(S) // 2:]:
      print(len(S))
      break

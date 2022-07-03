S = list(map(int, input()))

a = 0
for i in range(len(S)):
  if i % 2 == 0:
    if S[i] == 1:
      continue
    elif S[i] == 0:
      a += 1
  elif i % 2 != 0:
    if S[i] == 0:
      continue
    elif S[i] == 1:
      a += 1

b = 0
for i in range(len(S)):
  if i % 2 != 0:
    if S[i] == 1:
      continue
    elif S[i] == 0:
      b += 1
  elif i % 2 == 0:
    if S[i] == 0:
      continue
    elif S[i] == 1:
      b += 1

ans = min(a, b)

print(ans)

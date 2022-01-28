P = list(map(int, input().split()))

S = ""
for p in P:
  a = p + 96
  S += chr(a)


print(S)

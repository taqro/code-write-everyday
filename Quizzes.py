N, X = map(int, input().split())
S = list(input())

for i in range(len(S)):
  if S[i] == "o":
    X += 1
  elif S[i] == "x" and X != 0:
    X -= 1

print(X)
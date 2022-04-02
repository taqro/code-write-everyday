N = int(input())
S = list(input())

x = 0
max = 0
for i in range(N):
  if S[i] == "I":
    x += 1
  elif S[i] == "D":
    x -= 1
  if x > max:
    max = x

print(max)

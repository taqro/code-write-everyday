S = input()
T = input()

sum = 0
for i in range(3):
  if S[i] == T[i]:
    sum += 1

print(sum)

S = input()
min = 10 ** 9
for i in range(len(S) - 2):
  a = int(S[i] + S[i + 1] + S[i + 2])
  if min > abs(753 - a):
    min = abs(753 - a)

print(min)

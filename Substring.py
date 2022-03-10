S = list(input())
T = list(input())

max = 0
for i in range(len(S) - len(T) + 1):
  cnt = 0
  k = 0
  for j in range(len(T)):
    if S[i + k] == T[j]:
      cnt += 1
    k += 1
  if cnt > max:
    max = cnt

print(len(T) - max)

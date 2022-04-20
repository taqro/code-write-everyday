N, M = map(int, input().split())
S = list(input().split())
T = list(input().split())

i = 0
j = 0
while i < N:
  if S[i] == T[j]:
    print("Yes")
    j += 1
  else:
    print("No")
  i += 1

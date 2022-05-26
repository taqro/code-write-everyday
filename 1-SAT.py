N = int(input())
S = [""] * N
for i in range(N):
  S[i] = input()

arr1 = []
arr2 = []

for i in range(N):
  if S[i][0] == "!":
    arr2.append(S[i][1:])
  else:
    arr1.append(S[i])

set_1 = set(arr1)
set_2 = set(arr2)

set = set_1 & set_2

if len(set) == 0:
  print("satisfiable")
else:
  print(list(set)[0])

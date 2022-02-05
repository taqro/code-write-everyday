N = int(input())
S = list(map(int, input()))

for i in range(N):
  if S[i] == 1:
    if i % 2 == 0:
      print("Takahashi")
      break
    else:
      print("Aoki")
      break

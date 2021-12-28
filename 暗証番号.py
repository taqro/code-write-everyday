N = list(input())

ans = "SAME"

for i in range(len(N)):
  for j in range(len(N)):
    if N[i] != N[j]:
      ans = "DIFFERENT"
      break

print(ans)

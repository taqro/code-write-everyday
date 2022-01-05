N = int(input())
L = list(map(int, input().split()))

L.sort()
sum = 0
for i in range(N):
  for j in range(i + 1, N):
    for k in range(j + 1, N):
      if L[i] != L[j]:
        if L[j] != L[k]:
          if L[i] + L[j] > L[k]:
            sum += 1

print(sum)

N = int(input())
A = list(map(int, input().split()))

koma = [0] * N

P = 0

for i in range(N):
  for j in range(i + 1):
    if koma[j] >= 4:
      continue
    koma[j] += A[i]
    if koma[j] >= 4:
      P += 1

print(P)

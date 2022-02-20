A, B, W = map(int, input().split())

m = 10 ** 9
M = 0

for i in range(1, 1000000 + 1):
  if A * i <= 1000 * W and 1000 * W <= B * i:
    m = min(m, i)
    M = max(M, i)

if M == 0:
  print("UNSATISFIABLE")
else:
  print(m, M)

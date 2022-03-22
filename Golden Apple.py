N, D = map(int, input().split())


for i in range(1, N + 1):
  if i * (2 * D + 1) >= N:
    print(i)
    break


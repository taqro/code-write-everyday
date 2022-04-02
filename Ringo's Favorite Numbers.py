D, N = map(int, input().split())

if D == 0:
  if N < 100:
    print(N)
  else:
    print(N + 1)
elif D == 1:
  if N < 100:
    print(100 * N)
  else:
    print(100 * N + 100)
elif D == 2:
  if N < 100:
    print(100 ** 2 * N)
  else:
    print(100 ** 2 * N + 100 ** 2)

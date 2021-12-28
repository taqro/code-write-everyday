A, B = map(int, input().split())

for i in range(1, 1000):
  if A * i >= B:
    print(i)
    break

N = int(input())

for i in range(10 ** 5):
  if 2 ** i > N:
    print(i - 1)
    break

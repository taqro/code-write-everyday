N, K = map(int, input().split())

sum = 0
while N > 0:
  N = N // K
  sum += 1

print(sum)

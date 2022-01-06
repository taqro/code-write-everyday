N = int(input())

a = list(map(int, input().split()))

a.sort(reverse=True)

sum = 0

for i in range(2 * N):
  if i % 2 != 0:
    sum += a[i]
  else:
    continue

print(sum)

N, x = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

sum = 0
for i in range(N):
  if x >= a[i]:
    sum += 1
    x -= a[i]
  else:
    break

  if i == N - 1 and x != 0:
    sum -= 1

print(sum)

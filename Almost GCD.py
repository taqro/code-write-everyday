N = int(input())
A = list(map(int, input().split()))

ans = 0
max = 0

for i in range(2, 1001):
  sum = 0
  for a in A:
    if a % i == 0:
      sum += 1
  if max < sum:
    max = sum
    ans = i

print(ans)

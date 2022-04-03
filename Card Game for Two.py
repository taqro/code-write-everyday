N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
sum_A = 0
sum_B = 0
for i in range(N):
  if i % 2 == 0:
    sum_A += a[i]
  else:
    sum_B += a[i]

print(sum_A - sum_B)

N = int(input())

A = list(map(int, input().split()))

odd_sum = 0

for i in A:
  if i % 2 != 0:
    odd_sum += 1
# 奇数が偶数個ある場合
if odd_sum % 2 == 0:
  print("YES")
# 奇数が奇数個ある場合
elif odd_sum % 2 != 0:
  print("NO")

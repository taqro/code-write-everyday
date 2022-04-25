S = list(input())

sum_1 = 0
for i in range(1, 10):
  sum_1 += i

sum_2 = 0
for i in range(len(S)):
  sum_2 += int(S[i])


ans = sum_1 - sum_2

print(ans)

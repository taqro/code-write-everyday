N = int(input())

sum = 0
ans = 1
for i in range(N):
  sum += i
  if sum >= N:
    ans = i
    break

print(ans)

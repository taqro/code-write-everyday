A, B, K = map(int, input().split())

ans = []
cnt = 0
for i in range(1, 100 + 1):
  if A % i == 0 and B % i == 0:
    cnt += 1
    ans.append(i)

print(ans[-K])

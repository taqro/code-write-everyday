A, B = map(int, input().split())

ans = 0
for i in range(1, 21):
  if A + (A - 1) * (i - 1)   >= B:
    ans = i
    break

if B == 1:
  ans = 0
print(ans)

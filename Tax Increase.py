A, B = map(int, input().split())

ans = -1

for i in range(10 ** 4):
  if int(i * 0.08) == A and int(i * 0.1) == B:
    ans = i
    break

print(ans)

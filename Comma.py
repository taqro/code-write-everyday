N = list(input())

ans = 0
cnt = 0
if len(N) > 3:
  for i in range(4,len(N) + 1):
    L =  [ *N[-i:] ]
    cnt = len(L) // 3
    if len(L) % 3 == 0:
      cnt -= 1
    if i == len(N):
      M = int(L[0])
      L.remove(L[0])
      ans += ((int("".join(L)) + 1) + ((M - 1) * 10 ** (len(L))) ) * cnt
    else:
      ans += 9 * (10 ** (len(L) - 1)) * cnt

print(ans)

N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

ans = "No War"

x.sort()
y.sort()

if x[-1] < y[0]:
  pass
else:
  ans = "War"

if X < y[0] and x[-1] < Y:
  pass
else:
  ans = "War"

print(ans)

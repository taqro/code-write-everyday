n,k,x = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
for aa in a:
  cnt += aa//x
if k<=cnt:
  print(sum(a)-k*x)
else:
  rem = k-cnt
  a = [i%x for i in a]
  a = sorted(a, reverse=True)
  print(sum(a[rem:]))

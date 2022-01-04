N = int(input())
T, A = map(int, input().split())
h = list(map(int, input().split()))

min = 10 ** 9
ans = 0
for i in range(N):
  a = abs(A - (T - h[i] * 0.006))
  if min > a:
    min = a
    ans = i + 1

print(ans)

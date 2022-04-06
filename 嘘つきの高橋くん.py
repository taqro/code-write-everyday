N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))

ans = "YES"
for i in range(K):
  if P.count(P[i]) > 1:
    ans = "NO"
  if P[i] == a or P[i] == b:
    ans = "NO"

print(ans)

N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for i in range(N):
  if A[i] != X:
    ans.append(str(A[i]))

ans = " ".join(ans)
print(ans)

N = int(input())
S = list(input())

ans = 0
for i in range(1,N):
  T = set(S[0:i]) & set(S[i::])
  if len(T) > ans:
    ans = len(T)

print(ans)

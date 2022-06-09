N = int(input())
S = [""] * N
for i in range(N):
  S[i] = input()

S_arr = set(S)
arr = list(S_arr)
ans = len(arr)

print(ans)

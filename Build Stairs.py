N = int(input())
H = list(map(int, input().split()))

for i in range(N - 1)[::-1]:
  if H[i] > H[i + 1]:
    H[i] -= 1

ans = "Yes"
for i in range(N - 1):
  if H[i] > H[i + 1]:
    ans = "No"
    break

print(ans)

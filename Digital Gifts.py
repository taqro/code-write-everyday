N = int(input())
x = [""] * N
u = [""] * N
for i in range(N):
  x[i], u[i] = input().split()

ans = 0
for i in range(N):
  if u[i] == "JPY":
    ans += int(x[i])
  elif u[i] == "BTC":
    ans += 380000 * float(x[i])

print(ans)

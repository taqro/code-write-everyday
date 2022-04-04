H_1, W_1 = map(int, input().split())
H_2, W_2 = map(int, input().split())

ans = "NO"
if H_1 == H_2:
  ans = "YES"
elif H_1 == W_2:
  ans = "YES"
elif H_2 == W_1:
  ans = "YES"
elif W_1 == W_2:
  ans = "YES"

print(ans)

X = int(input())

ans = 0
amari = 0

ans += X // 500 * 1000
amari = X % 500

ans += amari // 5 * 5

print(ans)

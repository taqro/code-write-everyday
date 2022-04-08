n, m = map(int, input().split())

n = n % 12

x = 6 * m
y = 30 * n + m / 2

ans = min(abs(x- y), 360 - abs(x- y))

print(ans)


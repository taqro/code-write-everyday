a, b, c, d = map(int, input().split())

ans = max(a * c, b * d)
ans = max(ans, a * d)
ans = max(ans, b * c)

print(ans)



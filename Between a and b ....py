a, b, x = map(int, input().split())

def f(n):
  if n >= 0:
    return n // x + 1
  elif n == -1:
    return 0

print(f(b) - f(a - 1))

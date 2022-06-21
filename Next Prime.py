X = int(input())

def is_prime_number(x):
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

for i in range(X, X + 10 ** 3):
  if is_prime_number(i):
    print(i)
    break

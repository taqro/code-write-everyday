N = int(input())

if N < 10:
  print("0" + str(N))
elif N < 100:
  print(N)
elif 100 <= N:
  print(str(N)[1:])

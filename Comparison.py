A = input()
B = input()

if len(A) > len(B):
  print("GREATER")
elif len(A) < len(B):
  print("LESS")
elif len(A) == len(B):
  cnt = 0
  for i in range(len(A)):
    if int(A[i]) == int(B[i]):
      cnt += 1
    elif int(A[i]) > int(B[i]):
      print("GREATER")
      break
    elif int(A[i]) < int(B[i]):
      print("LESS")
      break
  if cnt == len(A):
    print("EQUAL")

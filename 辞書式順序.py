A = list(input())

if len(A) > 1:
  B = A[0:-1]
  print("".join(B))
elif len(A) and A[0] != "a":
  print(chr(ord(A[0]) - 1))
elif len(A) and A[0] == "a":
  print(-1)

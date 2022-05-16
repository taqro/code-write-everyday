A, B, C = map(int, input().split())

if A == B:
  print("=")
elif A >= 0 and B >= 0:
  if A > B:
    print(">")
  elif A < B:
    print("<")
else:
  if C % 2 == 0:
    if A == 0 or B == 0:
      if A == 0:
        print("<")
      else:
        print(">")
    elif abs(A) == abs(B):
      print("=")
    elif A < 0 and B < 0:
      if A < B:
        print(">")
      else:
        print("<")
    elif A < 0 and B > 0:
      if abs(A) > B:
        print(">")
      else:
        print("<")
    elif A > 0 and B < 0:
      if A < abs(B):
        print("<")
      else:
        print(">")
  else:
    if A == 0 or B == 0:
      if A == 0 and B > 0:
        print("<")
      elif A == 0 and B < 0:
        print(">")
      elif A > 0 and B == 0:
        print(">")
      elif A < 0 and B == 0:
        print("<")
    elif A < 0 and B < 0:
      if A < B:
        print("<")
      else:
        print(">")
    elif A < 0 and B > 0:
      print("<")
    elif A > 0 and B < 0:
      print(">")

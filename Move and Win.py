N, A, B = map(int, input().split())

cnt = 0
while cnt < 100001:
  cnt += 1
  if A == 1 and A + 1 == B:
    print("Borys")
    break
  elif A + 1 == B:
    A -= 1
  elif A == 1:
    A += 1
  else:
    A += 1
  if B == N and B - 1 == A:
    print("Alice")
    break
  elif B - 1 == A:
    B += 1
  elif B == N:
    B -= 1
  else:
    B -= 1
  if cnt == 100:
    print("Draw")
    break


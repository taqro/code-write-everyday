A, B, C = list(input().split())

max = int(A + B) + int(C)
if max < int(B + A) + int(C):
  max = int(B + A) + int(C)
if max < int(B + C) + int(A):
  max = int(B + C) + int(A)
if max < int(C + B) + int(A):
  max = int(C + B) + int(A)
if max <int(C + A) + int(B):
  max = int(C + A) + int(B)
if max <int(A + C) + int(B):
  max = int(A + C) + int(B)

print(max)

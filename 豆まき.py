A = int(input())
B = int(input())
C = int(input())

a = [A, B, C]
a.sort(reverse=True)

print(a.index(A) + 1)
print(a.index(B) + 1)
print(a.index(C) + 1)

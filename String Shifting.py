S = list(input())
T = []
for i in range(len(S)):
  value = S.pop(0)
  S.append(value)
  T.append("".join(S))

T.sort()

print(T[0])
print(T[-1])

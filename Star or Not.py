from collections import Counter
N = int(input())
a = [0] * (N - 1)
b = [0] * (N - 1)
for i in range(N - 1):
  a[i], b[i] = map(int, input().split())

c = [*a, *b]
d = Counter(c)
e = d.most_common()[0][0]
ans = "Yes"
for i in range(N - 1):
  if a[i] != e and b[i] != e:
    ans = "No"
    break

print(ans)

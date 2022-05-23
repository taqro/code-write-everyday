N, K = input().split()

N = list(N)
a = [N]

def f(i):
  a[i].sort(reverse=True)
  g_1 = int("".join(a[i]))
  a[i].sort()
  g_2 = int("".join(a[i]))
  return list(str(g_1 - g_2))


for i in range(int(K)):
  a.append(f(i))

print("".join(a[int(K)]))

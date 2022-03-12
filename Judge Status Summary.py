N = int(input())
S = [0] * N
for i in range(N):
  S[i] = input()

ans = [0] * 4

for i in range(N):
  if S[i] == "AC":
    ans[0] += 1
  if S[i] == "WA":
    ans[1] += 1
  if S[i] == "TLE":
    ans[2] += 1
  if S[i] == "RE":
    ans[3] += 1

print("AC x " + str(ans[0]))
print("WA x " + str(ans[1]))
print("TLE x " + str(ans[2]))
print("RE x " + str(ans[3]))

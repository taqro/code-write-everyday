x_1, y_1, x_2, y_2 = map(int, input().split())

ans = "No"
for i in range(50):
  for j in range(50):
    x = x_1 + i
    y = y_1 + j
    if (x - x_1) ** 2 + (y - y_1) ** 2 == 5 and (x - x_2) ** 2 + (y - y_2) ** 2 == 5:
      ans = "Yes"
      break
    x = x_1 + i
    y = y_1 - j
    if (x - x_1) ** 2 + (y - y_1) ** 2 == 5 and (x - x_2) ** 2 + (y - y_2) ** 2 == 5:
      ans = "Yes"
      break
    x = x_1 - i
    y = y_1 + j
    if (x - x_1) ** 2 + (y - y_1) ** 2 == 5 and (x - x_2) ** 2 + (y - y_2) ** 2 == 5:
      ans = "Yes"
      break
    x = x_1 - i
    y = y_1 - j
    if (x - x_1) ** 2 + (y - y_1) ** 2 == 5 and (x - x_2) ** 2 + (y - y_2) ** 2 == 5:
      ans = "Yes"
      break

print(ans)

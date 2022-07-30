N, A, B = map(int, input().split())
grid = []

for _ in range(5):
    for row in range(A):  # 1,3,5,7,9行目のタイル、タイルは縦A行なのでA回ループ
        grid.append(("." * B + "#" * B) * 5)  # 白から始まる
    for row in range(A):  # 2,4,6,8,10行目のタイル
        grid.append(("#" * B + "." * B) * 5)

# 答えはA * N行 B * N列です
for row in range(A * N):
    print(grid[row][:B * N])


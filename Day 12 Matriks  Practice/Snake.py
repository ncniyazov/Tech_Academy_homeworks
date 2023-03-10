n, m, x, y = (int(i) for i in input().split())
matrix = [[0] * m for i in range(n)]
k = 0

for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            matrix[i][j] = k
            k += 1
    else:
        for j in range(m - 1, -1, -1):
            matrix[i][j] = k
            k += 1

print(matrix[x - 1][y - 1])

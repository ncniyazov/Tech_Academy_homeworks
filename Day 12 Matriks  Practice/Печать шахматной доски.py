n = int(input())
matrix = [[0] * n for i in range(n)]
count = 1
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            matrix[i][j] = count
            count += 1
for i in range(n):
    for j in range(n):
        if (i + j) % 2 != 0:
            matrix[i][j] = count
            count += 1
for element in matrix:
    print(*element)
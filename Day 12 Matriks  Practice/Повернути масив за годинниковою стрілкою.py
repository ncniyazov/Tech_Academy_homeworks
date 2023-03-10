n = abs(int(input()))
matrix = [list(int(i) for i in input().split()) for i in range(n)]
for i in range(n):
    for j in range(n):
        print(matrix[-(j + 1)][i], end=' ')
    print()
n = int(input())
matrix = [list(int(i) for i in input().split()) for i in range(n)]
r, c = (int(i) for i in input().split())

for i in range(0,r):
    for j in range(0,c):
        print(matrix[i][j], end=" ")
    print()

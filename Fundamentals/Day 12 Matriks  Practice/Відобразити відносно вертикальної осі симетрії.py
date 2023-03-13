setir, sutun = (int(i) for i in input().split())
matrix = [list(int(i) for i in input().split()) for i in range(setir)]
for i in range(setir):
    for j in range(sutun):
        print(matrix[i][-(j+1)], end=' ')
    print()
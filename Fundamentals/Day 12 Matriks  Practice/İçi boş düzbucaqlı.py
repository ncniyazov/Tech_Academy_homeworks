n, m = (int(i) for i in input().split())
matrix =[]
for i in range(n):
    matrix.append(["*"] * m)
for setir in range(1, n-1):
    for star in range(1, m-1):
        matrix[setir][star] = " "
for setir in matrix:
    for star in setir:
        print(star, end="")
    print()
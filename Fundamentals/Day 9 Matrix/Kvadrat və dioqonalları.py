n = abs(int(input()))
matrix =[]
for i in range(n):
    matrix.append(["*"] * n)
for setir in range(1, n-1):
    for star in range(1, n-1):
        matrix[setir][star] = " "
        matrix[setir][setir] = "*"
        matrix[setir][-(setir + 1)] = "*"
for setir in matrix:
    for star in setir:
        print(star, end="")
    print()
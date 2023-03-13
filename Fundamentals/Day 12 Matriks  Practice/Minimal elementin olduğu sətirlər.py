setir, sutun = (int(i) for i in input().split())
matrix = [list(int(i) for i in input().split()) for i in range(setir)]
min_of_line = 100
for line in matrix:
    for el in line:
        if el < min_of_line:
            min_of_line = el
for l in range(0, setir):
    if min_of_line in matrix[l]:
        print(l+1, end=" ")

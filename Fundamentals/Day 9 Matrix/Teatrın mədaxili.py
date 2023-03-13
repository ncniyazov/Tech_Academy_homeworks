setir, sutun = (int(i) for i in input().split())
matrix_count = [list(int(i) for i in input().split()) for i in range(setir)]
br = input()
matrix_sold = [list(int(i) for i in input().split()) for i in range(setir)]
profit = 0
for setir in range(setir):
    for el in range(sutun):
        if matrix_sold[setir][el]:
            profit += matrix_count[setir][el]
print(profit)
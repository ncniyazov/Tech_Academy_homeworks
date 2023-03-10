setir, sutun = (int(i) for i in input().split())
matrix = [list(int(i) for i in input().split()) for i in range(setir)]
odd_counts = 0
for setir in matrix:
    for el in setir:
        if el %2 ==0:
            odd_counts += 1
print(odd_counts)

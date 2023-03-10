setir, sutun = (int(i) for i in input().split())
matrix = [list(int(i) for i in input().split()) for i in range(setir)]
even_sum = 0
for i in range(0, setir, 2):
    even_sum+=sum(matrix[i])
print(even_sum)

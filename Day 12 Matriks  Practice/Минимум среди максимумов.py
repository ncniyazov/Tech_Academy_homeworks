setir, sutun = (int(i) for i in input().split())
matrix = [list(int(i) for i in input().split()) for i in range(setir)]
max_numbers=[]
for i in range(0, setir):
    max_numbers.append(max(matrix[i]))
print(min(max_numbers))

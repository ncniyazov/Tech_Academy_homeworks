setir, sutun = (int(i) for i in input().split())
matrix = [list(int(i) for i in input().split()) for i in range(setir)]
max_lines = []
for i in range(setir):
    max_lines.append(sum(matrix[i]))
for line in range(0, setir):
    if sum(matrix[line]) == max(max_lines):
        print(line+1, end=" ")
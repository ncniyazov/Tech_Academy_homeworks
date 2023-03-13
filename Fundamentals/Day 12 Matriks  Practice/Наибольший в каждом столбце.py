n, m = (int(i) for i in input().split())
matrix = [list(int(i) for i in input().split()) for i in range(n)]

new_list = []
max_list = []
for j in range(m):
    for i in range(n):
        new_list.append(matrix[i][j])
    max_list.append(max(new_list))
    new_list = []
print (*max_list)
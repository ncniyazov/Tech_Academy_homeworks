n, m  = (int(i) for i in input().split())
matrix = [list(int(i) for i in input().split()) for i in range(n)]
total = 0
for row in matrix: total += sum(row)
print(total)

n = abs(int(input()))
matrix = [list(int(i) for i in input().split()) for i in range(n)]
diaqonal = []
ters_diaqonal = []
for i in range(0, n):
    diaqonal.append(matrix[i][i])
    ters_diaqonal.append(matrix[i][-(i+1)])
print(sum(diaqonal), sum(ters_diaqonal))
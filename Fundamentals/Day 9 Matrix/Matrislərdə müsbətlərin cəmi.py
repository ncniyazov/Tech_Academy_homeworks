n = abs(int(input()))
positives_sum = 0
matrix = [list(int(i) for i in input().split()) for i in range(n)]
for setir in matrix:
    for element in setir:
        if element > 0: positives_sum += element
print(positives_sum)
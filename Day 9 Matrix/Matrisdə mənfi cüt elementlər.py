n = abs(int(input()))
negatives_sum = 0
count = 0
matrix = [list(int(i) for i in input().split()) for i in range(n)]
for setir in matrix:
    for element in setir:
        if element < 0 and element % 2 == 0: 
            negatives_sum += element
            count += 1
print(count, negatives_sum)
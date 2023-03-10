n = abs(int(input()))
l = list(int(i) for i in input().split())
sum = 0
max_value = max(l)

for i in l:
    if i != max_value:
        sum += (i)
print(sum)

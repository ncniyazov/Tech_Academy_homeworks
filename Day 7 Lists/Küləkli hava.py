n = abs(int(input()))
l = list(int(i) for i in input().split())
max_i = l[0]
min_i = l[0]

for item in range(n):
    if l[item] > max_i:
        max_i = l[item]
    if l[item] < min_i:
        min_i = l[item]
        
print(max_i - min_i)

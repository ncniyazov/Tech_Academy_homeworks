n = abs(int(input()))
l = list(int(i) for i in input().split())
count = 0
max_value = max(l)

for i in l:
    if i == max_value:
        count += 1
print(count)

n = abs(int(input()))
l = list(int(i) for i in input().split())
count = 0
for i in range(n):
    if i == n-1:
        break
    if i > 0:
        if l[i] > l[i-1] and l[i] > l[i+1]:
            count += 1
    
print(count)
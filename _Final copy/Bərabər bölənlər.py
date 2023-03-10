n = abs(int(input()))
count = 0
for m in range(1, n):
    if n%m == n//m:
        count += 1
        
print(count)
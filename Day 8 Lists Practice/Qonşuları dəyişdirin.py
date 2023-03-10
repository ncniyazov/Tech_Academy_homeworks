n = abs(int(input()))
siyahi = list(int(i) for i in input().split())
for i in range(0, n-1, 2):
    siyahi[i], siyahi[i+1] = siyahi[i+1], siyahi[i]
    
print(*siyahi)
n = abs(int(input()))
siyahi = list(int(i) for i in input().split())
max_val = max(siyahi)
min_val = min(siyahi)

for i in range(n):
    if siyahi[i] == max_val:
        siyahi[i] = min_val
    elif siyahi[i] == min_val:
        siyahi[i] = max_val
        
print(*siyahi)
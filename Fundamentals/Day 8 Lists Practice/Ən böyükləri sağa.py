n = abs(int(input()))
siyahi = list(int(i) for i in input().split())
sum = 0
for i in range(n):
    if siyahi[i] == max(siyahi):
        siyahi.append(siyahi[i])
        siyahi.remove(siyahi[i])
print(*siyahi)
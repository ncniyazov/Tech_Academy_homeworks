n = abs(int(input()))
siyahi = list(int(i) for i in input().split())
siyahi.reverse()
for i in range(n):
    if siyahi[i] == min(siyahi):
        siyahi.append(siyahi[i])
        siyahi.remove(siyahi[i])
siyahi.reverse()
print(*siyahi)
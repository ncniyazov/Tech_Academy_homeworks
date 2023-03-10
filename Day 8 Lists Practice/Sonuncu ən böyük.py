n = abs(int(input()))
siyahi = list(int(i) for i in input().split())
max_index = -1
for i in range(n):
    if max_index == -1 or siyahi[i] >= siyahi[max_index]:
        max_index = i
siyahi[max_index], siyahi[n - 1] = siyahi[n - 1], siyahi[max_index]
print(*siyahi)
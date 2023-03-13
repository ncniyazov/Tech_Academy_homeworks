n = abs(int(input()))
siyahi = list(int(i) for i in input().split())
restored_arr = [i - (max(siyahi) - min(siyahi)) for i in siyahi]
print(*restored_arr)
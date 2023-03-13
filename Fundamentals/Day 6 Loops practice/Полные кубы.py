n = abs(int(input()))

for item in range(1, n):
    kub = item**3
    if kub >= n:
        break
    print(kub, end=' ')

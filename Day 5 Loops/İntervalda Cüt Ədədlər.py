a, b = (int(i) for i in input().split())
for i in range(b, a - 1, -1):
    if i % 2 == 0:
        print(i, end=" ")

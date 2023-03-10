n = abs(int(input()))
l = list(int(i) for i in input().split())

for i in range(0, len(l), 2):
    print(l[i], end=" ")
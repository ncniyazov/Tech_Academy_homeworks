n = abs(int(input()))
l = list(int(i) for i in input().split())

for i in l:
    if i%2 > 0:
        print(i, end=" ")
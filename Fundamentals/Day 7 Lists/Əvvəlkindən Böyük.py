n = abs(int(input()))
l = list(int(i) for i in input().split())
start = l[0]
ends = l[-1]
for i in range(1, len(l)):
    if l[i] > l[i-1]:
        print(l[i], end=" ")
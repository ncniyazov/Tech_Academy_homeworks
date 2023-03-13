n = abs(int(input()))
l = list(int(i) for i in input().split())
start = l[0]
ends = l[-1]
for i in range(1, n):
    if l[i] > 0 and l[i - 1] > 0 or l[i] < 0 and l[i - 1] < 0:
        print(l[i-1], l[i])
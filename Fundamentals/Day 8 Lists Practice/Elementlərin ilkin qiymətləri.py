n = abs(int(input()))
l = list(int(i) for i in input().split())
en_kicik  = min(l)//2
for i in range(n):
    l[i] -= en_kicik
    print(l[i], end=" ")

    
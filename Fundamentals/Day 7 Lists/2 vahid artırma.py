n = abs(int(input()))
l = list(int(i) for i in input().split())

for item in range(n):
    if l[item] >= 0:
        n_plus2 = l[item] + 2
        print(n_plus2, end=" ")
    else:
        num = l[item]
        print(num, end=" ")

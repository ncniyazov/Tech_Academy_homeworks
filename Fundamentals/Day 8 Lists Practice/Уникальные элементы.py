n = abs(int(input()))
l = list(int(i) for i in input().split())
my_list = []
for i in range(n):
    if l.count(l[i]) > 1:
        pass
    else:
        my_list.append(l[i])

print(*my_list)
n = abs(int(input()))
l = list(int(i) for i in input().split())
min_index = l.index(min(l))
new_list = l.copy()
new_list[0] = min(l)
new_list[min_index] = l[0]
new_list[0] = min(l)
print(*new_list)
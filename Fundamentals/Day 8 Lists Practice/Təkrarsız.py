n = abs(int(input()))
l = list(int(i) for i in input().split())
my_list = []
for i in l:
    if i not in my_list:
        my_list.append(i)

print(*my_list)
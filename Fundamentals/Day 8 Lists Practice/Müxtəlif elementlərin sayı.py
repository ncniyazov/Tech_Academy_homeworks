n = abs(int(input()))
l = list(int(i) for i in input().split())
my_list = []
for i in l:
    if i in my_list:
        pass
    else:
        my_list.append(i)
        
print(len(my_list))
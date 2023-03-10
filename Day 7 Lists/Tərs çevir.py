n = abs(int(input()))
num_list = []
for item in range(n):
    num = (int(input()))
    num_list.append(num)
num_list_rev = num_list[::-1]     
for i in num_list_rev:
    print(i, end=" ")        


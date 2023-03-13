n = int(input())
interesting_list = []
for i in range(n):
    interesting_list.append(i+1)
    interesting_list.reverse()
    
print(*interesting_list)
    
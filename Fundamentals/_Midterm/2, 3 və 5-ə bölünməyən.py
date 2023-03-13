n = int(input())
i = 1
count = 0
while True:
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        print(i, end=" ")
        count += 1
        
    if count >= n:
        break    
    i += 1
    
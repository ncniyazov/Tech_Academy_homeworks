n = abs(int(input()))
count = 0 
while n >= 1: # 12 6 3 
    if n == 1:
        break
    if n % 2 == 0:
        n /= 2
    else:
        n += 1
    
    count += 1     
    
print(count)
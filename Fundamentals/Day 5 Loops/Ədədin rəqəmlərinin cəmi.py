n = abs(int(input()))
count = 0
while n > 0:
    last = n % 10  
    count += last
    n //= 10
print(count)
n = int(input())

_sum = 0

if n == 0:
    print(1)
else:   
    while n > 0:
        n //=  10
        _sum += 1
print(_sum)
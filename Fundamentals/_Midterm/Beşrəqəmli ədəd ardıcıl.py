n = abs(int(input()))
first = n // 10000
second = n % 10000 // 1000
third = n % 1000 // 100
fourth = n % 100 // 10
last = n % 10
result = 'NO'
if first < second < third < fourth < last:
    result = "YES"

print (result)
n = int(input())
first = n // 1000
second = n % 1000 // 100
third = n % 100 // 10
last = n % 10

print(first * first + second * second + third * third + last * last)
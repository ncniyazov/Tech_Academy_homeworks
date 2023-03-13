n = int(input())
first = n // 10000
qaliq1 = n % 1000
third = qaliq1 // 100
last = n % 10

print(first * 100 + third *10 + last)

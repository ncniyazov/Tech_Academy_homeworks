n = int(input())
first = n // 100
last = n % 10
mid = n % 100 // 10
print(mid * 100 + first * 10 + last)

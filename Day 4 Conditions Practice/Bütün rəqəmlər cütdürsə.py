n = int(input())
first = n // 1000
second = n % 1000 // 100
third = n % 100 // 10
last = n % 10

if first % 2 == 0 and second % 2 == 0 and third % 2 == 0 and last % 2 == 0:
    print("YES")
else:
    print("NO")
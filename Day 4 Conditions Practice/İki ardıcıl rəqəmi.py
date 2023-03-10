n = int(input())
first = n // 1000
second = n % 1000 // 100
third = n % 100 // 10
last = n % 10
if first == 3 and second == 7 or second == 3 and third == 7 or third == 3 and last == 7:
    print("YES")
else:
    print("NO")
a, b = (int(i) for i in input().split())

for i in range(a, b + 1):
    n = i
    first = (n // 1000)
    second = (n % 1000 // 100)
    third = (n % 100 // 10)
    last = (n % 10)
    if first % 2 > 0 and second % 2 > 0 and third % 2 > 0 and last % 2 > 0:
        print(n, end=" ")


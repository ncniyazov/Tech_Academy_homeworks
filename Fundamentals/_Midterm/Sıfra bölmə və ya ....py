a, b = (int(i) for i in input().split())
if b == 0:
    print("ERROR")
else:
    t = a // b
    print(t)

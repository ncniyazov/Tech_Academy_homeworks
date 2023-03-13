n, a, b = (int(i) for i in input().split())
if n % a == 0 and n % b == 0:
    print("YES")
else:
    print("NO")

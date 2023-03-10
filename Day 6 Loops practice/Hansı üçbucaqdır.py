a, b, c= (int(i) for i in input().split())
if a == b and b == c and c == a: 
    print(1) 
elif a == b or b == c or c == a: 
    print(2)
else:
    print(3) 
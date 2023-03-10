a, b, c= (abs(int(i)) for i in input().split())
try_a = (b*b + c*c)**(1/2)
try_b = (a*a + c*c)**(1/2)
try_c = (b*b + a*a)**(1/2)
if a == try_a or b == try_b or c == try_c:
    print("YES")
else:
    print("NO")

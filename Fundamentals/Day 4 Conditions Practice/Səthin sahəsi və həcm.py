a, b, c = (int(i) for i in input().split())
s = 2 * (a*b + b*c + c*a)
v = a * b * c
print(s, v)

a, b, c = (int(i) for i in input().split())
ab = a + b
ac = a + c
bc = c + b
print("YES") if ab > c and bc > a and ac > b else print("NO")


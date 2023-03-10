r, w, l = (int(i) for i in input().split())
diametr = 2 * r
diaqonal = (w*w + l*l)**(1/2)
if diametr >= diaqonal:
    print("YES")
else:
    print("NO")

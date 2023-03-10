h, w, l, k = (int(i) for i in input().split())
v = h * w * l
bat_count = v // k
if v % k == 0:
    print(bat_count)
else:
    print(bat_count+1)
    

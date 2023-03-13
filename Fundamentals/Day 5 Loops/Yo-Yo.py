l, k = (int(i) for i in input().split())
count = 0
while l > 1:
    #print(l)
    l /= k
    count += 1
print(count-1)
    
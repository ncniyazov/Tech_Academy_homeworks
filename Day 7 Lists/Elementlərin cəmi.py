n = abs(int(input()))
l = list(float(i) for i in input().split())
sum = 0
for i in l:
    sum += float(i)

print('%.1f' % sum)

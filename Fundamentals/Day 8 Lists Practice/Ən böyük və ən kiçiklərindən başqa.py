n = abs(int(input()))
l = list(int(i) for i in input().split())
sum = 0
for i in l:
    if i == max(l) or i == min(l):
        pass
    else:
        sum += i
        
print(sum)
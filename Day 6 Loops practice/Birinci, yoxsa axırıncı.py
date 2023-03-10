n = int(input())
first = n // 100
last = n % 10    
if first > last:
    print (first)
elif first < last:
    print (last)
else:
    print("=")
n = int(input())
first = n // 1000
second = n % 1000 // 100
third = n % 100 // 10
last = n % 10
#print(first, second, third, last)
if first != 0 and second != 0 and third != 0 and last != 0:
    if n % first == 0 and n % second == 0 and n % third == 0 and n % last == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

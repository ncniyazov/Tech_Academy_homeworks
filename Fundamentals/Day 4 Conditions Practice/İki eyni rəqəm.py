n = int(input())
first = (n // 1000)
second = (n % 1000 // 100)
third = (n % 100 // 10)
last = (n % 10)

#print(first, second, third, last)
if first != 0 or second != 0 or third != 0 or last != 0:

    if first == second and third == last or first == third and second == last or first == last and third == second:

        print("YES")
    else:
        print("NO")
else:
    print("NO")

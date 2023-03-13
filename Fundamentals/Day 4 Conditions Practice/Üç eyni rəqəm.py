n = int(input())
first = str(n // 1000)
second = str(n % 1000 // 100)
third = str(n % 100 // 10)
last = str(n % 10)
n_str = str(n)
#print(message.count('p'))
if n_str.count(first) == 3 or n_str.count(second) == 3 or n_str.count(third) == 3 or n_str.count(last) == 3: 
    print("YES")
else:
    print("NO")
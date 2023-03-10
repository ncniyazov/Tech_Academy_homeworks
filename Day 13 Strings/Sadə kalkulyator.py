s = input().split(" ")
emeliyyat = s[1]
first = int(s[0])
last = int(s[-1])
if emeliyyat == "*":
    print(first * last)
if emeliyyat == "-":
    print(first - last)
if emeliyyat == "+":
    print(first + last)
if emeliyyat == "/":
    print(first // last)
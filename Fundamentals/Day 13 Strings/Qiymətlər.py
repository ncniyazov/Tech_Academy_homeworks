s = input().lower().strip()
two = s.count("2")
five = s.count("5")
if two > five:
    print(2)
if two == five:
    print("=")
if two < five:
    print(5)
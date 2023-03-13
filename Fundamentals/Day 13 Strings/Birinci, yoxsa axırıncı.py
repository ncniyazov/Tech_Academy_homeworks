s = input()
chars = []
first = int(s[0])
last = int(s[-1])
if first == last:
    print("=")
else:
    print(max(first, last))
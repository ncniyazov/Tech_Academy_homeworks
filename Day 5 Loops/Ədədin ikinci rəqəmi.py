n = abs(int(input()))
l = len(str(n))

num = n // (10 ** (l-2)) % 10
print(num)

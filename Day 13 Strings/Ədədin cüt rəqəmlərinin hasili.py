n = input()
product = 1

for digit in n:
    if digit.isdigit() and int(digit) % 2 == 0:
        product *= int(digit)

if product == 1:
    print("-1")
else:
    print(product)

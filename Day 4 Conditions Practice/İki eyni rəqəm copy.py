n = int(input())
digits = [0] * 10  # Create a list to store the count of each digit
for d in str(n):
    digits[int(d)] += 1  # Increment the count of the current digit
if 2 in digits and digits.count(2) == 2:  # Check if there are exactly 2 digits that occur twice
    print("YES")
else:
    print("NO")
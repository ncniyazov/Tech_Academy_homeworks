correct_number = abs(int(input()))
odd_sum = 0
even_sum = 0
while correct_number:
    odd_sum += correct_number % 10
    correct_number //= 10
    even_sum += correct_number % 10
    correct_number //= 10
print(even_sum * odd_sum)

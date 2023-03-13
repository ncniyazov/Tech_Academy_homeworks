n = abs(int(input()))
n = n * 2 - 1
for i in range(n):
    for j in range(n):
        if j == i or j == n - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
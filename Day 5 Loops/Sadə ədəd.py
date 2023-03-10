n = int(input())
netice = "Yes"
if n <= 1:
    netice = "No"
else:
    for i in range(2, int((n**0.5)) + 1):
        if n % i == 0:
            netice = "No"
            break
print(netice)

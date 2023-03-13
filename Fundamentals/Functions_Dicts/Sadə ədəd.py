def primeNumb(n):
    netice = "Yes"
    if n <= 1:
        netice = "No"
    else:
        for i in range(2, int((n**0.5)) + 1):
            if n % i == 0:
                netice = "No"
                break
    return netice

def main():
    print(primeNumb(abs(int(input()))))


if __name__ == '__main__':
    main()

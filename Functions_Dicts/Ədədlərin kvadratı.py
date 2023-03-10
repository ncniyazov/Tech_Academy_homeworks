n = abs(int(input()))
numbers = []


def numbersSquares(numb):
    i = 1
    while i**2 <= numb:
        numbers.append(i**2)
        i += 1
    return numbers


def main():
    print(*numbersSquares(n))


if __name__ == '__main__':
    main()

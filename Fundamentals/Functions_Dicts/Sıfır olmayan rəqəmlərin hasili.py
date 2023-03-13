def powerNums(num):
    power = 1
    for i in list(num):
        if int(i) > 0:
            power *= int(i)
    return power

def main():
    print(powerNums(input()))


if __name__ == '__main__':
    main()

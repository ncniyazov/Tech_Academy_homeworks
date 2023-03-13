x, y, z = [float(i) for i in input().split()]

def minOfList(*args):
    return min(max(args[0], args[1]), max(args[1], args[2]), sum(args))


def main():
    print(minOfList(x, y, z))


if __name__ == '__main__':
    main()

lst = list(int(i) for i in input().split())


def rectangle_area(params):
    return params[0] * params[1]


def main():
    print(rectangle_area(lst))


if __name__ == '__main__':
    main()

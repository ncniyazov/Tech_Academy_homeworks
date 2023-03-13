n = abs(int(input()))

def rev_nums(n):
    num_list = []
    for item in range(n):
        num = (int(input()))
        num_list.append(num)
    num_list_rev = num_list[::-1]
    return num_list_rev

def print_elements():
    lst = rev_nums(n)
    for i in lst:
        print(i, end=" ")

def main():
    print_elements()

if __name__ == '__main__':
    main()

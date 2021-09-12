# TODO: Write recursive print_num_pattern() function
def print_num_pattern(n1, n2):
    print(n1, end=' ')
    if n1 > 0:
        print_num_pattern(n1 - n2, n2)
        print(n1, end=' ')

if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print_num_pattern(num1, num2)

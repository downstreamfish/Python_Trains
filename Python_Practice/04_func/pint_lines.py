def print_line(char, times):
    print(char * times)


def print_lines(char, times, lines):
    while lines > 0:
        print(char * times)
        lines -= 1

def test():
    print_line('*', 30)
    print_line('-', 35)
    print_line('=', 40)
    print_lines('~',50, 5)

if __name__ == '__main__':
    test()

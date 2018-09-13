def multiple_table():
    row = 1

    while row <= 9:
        col = 1
        while col <= row:
            print('{0} * {1} = {2}\t'.format(row, col, row * col), end="")
            col += 1
        print()
        row += 1

def test():
    multiple_table()

if __name__ == '__main__':
    test()

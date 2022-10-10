def print_operation_table(operation, num_rows=9, num_columns=9):
    for i in range(num_rows):
        for j in range(num_columns):
            print(f'{operation(i + 1, j + 1)}', end=' \t')
        print()


print_operation_table(lambda x, y: x * y)
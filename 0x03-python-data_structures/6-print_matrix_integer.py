def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        x = 0
        for x in range(len(matrix)):
            print("{} ".format(matrix[i][x]), end='')
        print()

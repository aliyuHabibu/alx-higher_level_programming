def no_c(my_string):
    for i in range(len(my_string)):
        if (my_string[i] == 'c') or (my_string == 'C'):
            my_string.pop(i)

    return my_string

def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return new_list
    else:
        new_list.pop(idx)
        new_list.insert(idx, element)
        return new_list

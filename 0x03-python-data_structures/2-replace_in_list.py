def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    else:
        my_list.pop(idx)
        my_list.insert(idx, element)
        return my_list

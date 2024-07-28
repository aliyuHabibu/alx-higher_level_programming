def add_tuple(tuple_a=(), tuple_b=()):
    answer_tuple = [0]
    append = 0
    t = []
    f = ()
    if ((len(tuple_a) <= 2) and (len(tuple_b) <= 2)):
        if (len(tuple_a) < 2):
            for i in range(2):
                tuple_a + tuple(append)
        if (len(tuple_b) < 2):
            for x in range(2):
                tuple_b + tuple(append)
        for n in range(0,2):
            r = tuple_a[n] + tuple_b[n]
            t.append(r)
        f = tuple(t)
        #answer_tuple + f
        return f
    else:
        for n in range(0,2):
            r = tuple_a[n] + tuple_b[n]
            t.append(r)
        f = tuple(t)
        #answer_tuple + f
        return f

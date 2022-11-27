def count_lst_odd(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0] % 2
    else:
        return lst[0] % 2 + count_lst_odd(lst[1:])
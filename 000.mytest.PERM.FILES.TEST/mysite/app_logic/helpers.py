def check_access_by_age(age):
    if age < 15:
        return False
    return True


def working_time(h):
    if 8 <= h < 13 or 14 <= h < 22:
        return True
    return False


def devider(n1, n2):
    res = True
    try:
        n1 / n2
    except ZeroDivisionError:
        res = False
    return res


def join_str(str_1, str_2):
    res = True
    try:
        str_1 + str_2
    except TypeError:
        res = False
    return res

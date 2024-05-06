#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for element in my_list:
            try:
                if isinstance(element, int):
                    print("{:d}".format(element), end="")
                    count += 1
                    if count == x:
                        break
            except (ValueError, TypeError):
                    pass
    except IndexError:
        print("IndexError: list index out of range")
    finally:
        print()
        return (count)

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                division = 0
            else:
                if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                    print("wrong type")
                    division = 0
                elif my_list_2[i] == 0:
                    print("division by 0")
                    division = 0
                else:
                    division = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            division = 0
        finally:
            result.append(division)
    return (result)


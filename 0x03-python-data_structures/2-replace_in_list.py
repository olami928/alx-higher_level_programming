<<<<<<< HEAD
#!/usr/bin/pyhton3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
=======
#!/usr/bin/python3
# this code replaces an element at a particular index

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return(my_list)
    else:
        my_list[idx] = element
        return(my_list)
>>>>>>> d8bc5057317dbe37eb0291c9e1e69e59d5947942

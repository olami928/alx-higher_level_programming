#!/usr/bin/python3
# his program prints a list at a particular index
if __name__ == "__main__":
    def element_at(my_list, idx):
        if idx < 0 or idx > len(my_list):
            return(None)
        else:
            return(my_list[idx])

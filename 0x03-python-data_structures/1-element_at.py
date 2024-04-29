#!/usr/bin/pythom3
#this program prints a list at a particular index
if __name__ == "__main__":
    def element_at(my_list, idx):
        if idx < 0 or idx > len(my_list):
            return(None)
        else:
            print(my_list[idx])

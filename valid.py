#This file will contain all of the validation functions to ensure that the
#user does not enter in the wrong values. 

def three_valid(choice):
    if choice == 1 or choice == 2 or choice == 3:
        return True
    else:
        return False

def two_valid(choice):
    if choice == 1 or choice == 2:
        return True
    else:
        return False

def start_valid(choice):
    if choice == 1 or choice == 2 or choice == 3 or choice == 4 or \
    choice == 5 or choice == 6 or choice == 7:
        return True
    else:
        return False

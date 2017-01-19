#importing all libraries which will be used.
import pandas as pd
import numpy as np

#importing all files that will be used in this program.
from valid import *
from support import *

####### Main Program functions here. #########

#This is the main function of the program that will start it and make it run.
def main():
    print('\033c')
    print()
    print('---------------------------')
    print('Welcome to Police Shootings')
    print('---------------------------')
    print()
    print('1. Use program')
    print('2. Information')
    print('3. Quit')
    support = Support()
    choice = int(input('What is your choice? '))
    while not three_valid(choice):
        print('That was not an acceptable choice')
        choice = int(input('What is your choice? '))
    if choice == 1:
        start()
    elif choice == 2:
        support.information()
        choice = support.menu()
        if choice == 1:
            main()
        elif choice == 2:
            support.quit()
    elif choice == 3:
        support.quit()

def start():
    print('\033c')




main()

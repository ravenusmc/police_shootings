#importing all libraries which will be used.
import pandas as pd
import numpy as np

#importing all files that will be used in this program.
from valid import *
from support import *
from data import *

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
        start(support)
    elif choice == 2:
        support.information()
        choice = support.menu()
        if choice == 1:
            main()
        elif choice == 2:
            support.quit()
    elif choice == 3:
        support.quit()

#This function will allow the user to choose what they want to do.
def start(support):
    print('\033c')
    #Creating the object which will contain all of the data from the CSV file.
    data = Data()
    print('1. Look at total U.S. deaths')
    print('2. Look at death by state')
    print('3. Look at graph of African American deaths')
    print('4. Conclusion')
    print('5. Quit')
    choice = int(input('What is your choice? '))
    if choice == 1:
        data.total_police_deaths()
        start(support)
    elif choice == 2:
        data.death_by_state()
        start(support)
    elif choice == 3:
        data.graph_deaths_african_american()
        start(support)
    elif choice == 4:
        support.conclusion()
        start(support)
    elif choice == 5:
        support.quit()


main()

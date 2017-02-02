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
    print()
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
    #Presenting options to the user on what they want to do
    print('1. Look at total U.S. deaths')
    print('2. Look at deaths by state')
    print('3. Look at threat level data')
    print('4. Look at graph of African American deaths')
    print('5. Look at graph of caucasian deaths')
    print('6. Conclusions')
    print('7. Quit')
    choice = int(input('What is your choice? '))
    if choice == 1:
        data.total_police_deaths()
        data.looking_deeper()
        start(support)
    elif choice == 2:
        data.death_by_state()
        start(support)
    elif choice == 3:
        threat_level(data, support)
    elif choice == 4:
        data.graph_deaths_african_american()
        start(support)
    elif choice == 5:
        data.graph_deaths_caucasian()
        start(support)
    elif choice == 6:
        support.conclusion()
        start(support)
    elif choice == 7:
        support.quit()

def threat_level(data, support):
    print('\033c')
    print('This section will allow you to look at various factors of threat level')
    print('In this case, threat level, means if the individual was attacking')
    print('1. All Data looking at threat level')
    print('2. Data looking at threat level and African Americans')
    print('3. Data looking at threat level and Caucasian')
    choice = int(input('What is your choice? '))
    if choice == 1:
        data.all_threat()
        start(support)


main()

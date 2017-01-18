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
        information(support)
    elif choice == 3:
        support.quit()

def start():
    print('\033c')


def information(support):
    print('\033c')
    print('''
    This project has two main purposes. The first to improve my skills using
    Pandas for Data Science projects. The second is that I am fascinated with
    social issues. (I have a history/political science background.) Thus,
    this project I may be able to learn about a social issue a little bit
    more as I improve my coding skills. If the user has questions or feedback
    please contact me on Github at https://github.com/ravenusmc. Thank you
    for taking the time to look at this project.
    ''')
    input('Press enter to continue ')
    choice = support.menu()
    if choice == 1:
        main()
    elif choice == 2:
        support.quit()



main()

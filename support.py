#This file will contain the class for my support functions

#importing files to use in this program
from valid import *

class Support():

    #This method will allow the user to quit the program
    def quit(self):
        print('\033c')
        print()
        print('Sorry to see you go!')
        print('Please come back soon!')
        print()

    #This method will allow the user to go back to the main menu in the program
    def menu(self):
        print('\033c')
        print('1. Main Menu')
        print('2. Quit ')
        choice = int(input('What is your choice? '))
        while not two_valid(choice):
            print('That is not a valid selection')
            choice = int(input('What is your choice? '))
        return choice 

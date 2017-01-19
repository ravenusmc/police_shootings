#This file will contain the class for my support functions

#importing files to use in this program
from valid import *

#This class will have all of the methods that will be called that provide
#support to the program.
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

    #This method will show the user some background information as to why I
    #choose to do this project.
    def information(self):
        print('\033c')
        print('''
        This project has two main purposes. The first to improve my skills using
        Pandas for Data Science projects. The second is that I am fascinated
        with social issues. (I have a history/political science background.)
        Thus, this project I may be able to learn about a social issue a little
        bit more as I improve my coding skills. If the user has questions or
        feedback please contact me on Github at https://github.com/ravenusmc.
        Thank you for taking the time to look at this project.
        ''')
        input('Press enter to continue ')

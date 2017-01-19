#importing all libraries which will be used.
import pandas as pd
import numpy as np

#importing validation file
from valid import *

#This class sets up the data frame and contains all the methods to act
#on that data frame.
class Data():

    #I have made the data attribute private to protect the information.
    def __init__(self):
        self.__data = pd.read_csv('database.csv')

    #This method will allow me to see all of the information that is contained
    #in games.
    def show(self):
        return self.__data

    #This method will allow the user to look at number of police deaths by
    #state
    def death_by_state(self):
        print('\033c')
        print('Here you will see police shootings by state')
        state = input('Please enter abbreviation for the state: ')
        state = state.upper()
        self.__data = self.__data[self.__data.state == state]
        count = len(self.__data)
        black = self.__data[self.__data.race == 'B']
        white = self.__data[self.__data.race == 'W']
        black_count = len(black)
        white_count = len(white)
        print()
        print(state, 'has', count, 'people dead by police shootings')
        print(black_count, 'Out of a total of', count, 'people were black')
        print(white_count, 'Out of a total of', count, 'people were white')
        print('The rest of the people were from different groups.')
        print()
        input('Press enter to continue')

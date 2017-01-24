#importing all libraries which will be used.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from collections import Counter
import operator
import collections

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

    #This method will show the total amount of people killed by police in the
    #United States.
    def total_police_deaths(self):
        print('\033c')
        self.__total_deaths = len(self.__data)
        self.__black = self.__data[self.__data.race == 'B']
        self.__white = self.__data[self.__data.race == 'W']
        self.__black_count = len(self.__black)
        self.__white_count = len(self.__white)
        print('The total police shootings, from January of 2015 to Decembr of 2016,')
        print('is the following:', self.__total_deaths)
        print()
        input('Press enter to see data broken down by race ')
        print()
        print(self.__black_count, 'Out of a total of', self.__total_deaths, 'people were black')
        print(self.__white_count, 'Out of a total of', self.__total_deaths, 'people were white')
        print()
        self.__black = self.__data[(self.__data.armed == 'unarmed')  & (self.__data.race == 'B')]
        self.__white = self.__data[(self.__data.armed == 'unarmed') & (self.__data.armed == 'W')]
        self.__unarmed_count_black = len(self.__black)
        self.__unarmed_count_white = len(self.__white)
        print()
        input('Press enter to see data broken down by armed and unarmed ')
        print()
        print(self.__unarmed_count_black, 'Out of', self.__black_count, 'blacks were unarmed.')
        print(self.__unarmed_count_white, 'Out of', self.__white_count, 'whites were unarmed.')
        print()
        input('Press Enter to continue ')

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
        print('The rest of the people are from different groups.')
        print()
        input('Press enter to continue')

    #This method will show a graph of african american deaths by police.
    def graph_deaths_african_american(self):
        print('\033c')
        print('A graph will appear showing you deaths of African Americans')
        print('by the police.')
        print()
        print('Once you are done looking at the graph, it must be closed to move on')
        input('Press Enter to continue')
        #Here I am setting up a list to hold all of the dates.
        dates = []
        #This start variable will act as a counter for the while loop.
        start = 0
        #The loop will start at 0 and go for the length of the data.
        while start < len(self.__data):
            #Here I am setting up the date variable to get a specific date
            date = datetime.strptime(self.__data.iat[start, 2], "%Y-%m-%d")
            race = self.__data.iat[start, 7]
            if race == 'B':
                #I want to only look at the dates where African Americans were
                #killed so I append those dates to the dates list.
                dates.append(date)
            #The start counter is increased by one for each cycle of the loop.
            start += 1
        #This code here will create a dictionary, named number_deaths. The
        #counter method is used to count the number of times each date appears.
        #I need to do this because the dates list may have numerous dates in it
        #for the same date. That will tell me that multiple people died on the
        #same date.
        number_deaths = Counter(dates)
        #The number_deaths dictionary is not sorted so the below line will
        #sort the information into the sorted_values dictionary.
        sorted_values = collections.OrderedDict(sorted(number_deaths.items()))
        #I then create two new lists which will have the information from the
        #sorted_values dictionary placed into these two lists.
        dates = []
        deaths = []
        #I use a for loop to loop through all of the entries in the sorted_values
        #dictionary.
        for item in sorted_values:
            dates.append(item)
            deaths.append(sorted_values[item])
        #The below lines of code is what will actually create the graph.
        fig = plt.figure(dpi=128, figsize=(10,6))
        plt.plot(dates, deaths, linewidth=2, c="red")
        plt.title("African American Deaths from Police", fontsize=24)
        plt.xlabel('Date', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Deaths", fontsize=16)
        plt.show()
        print()
        #The following lines of code get the mean for the data and then I display
        #that mean.
        total = sum(deaths)
        print(len(deaths))
        mean = total / len(deaths)
        print('The average deaths per day is the following', mean)
        input('Press Enter to continue to return to main menu ')

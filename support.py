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
        print('\t~~~~~~~~~~~~~~~~~~~~~~~~')
        print('\tSorry to see you go!')
        print('\tPlease come back soon!')
        print('\t~~~~~~~~~~~~~~~~~~~~~~~~')
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

    #This method will show the user some of the conclusions that I have drawn
    #from this project.
    def conclusion(self):
        print('\033c')
        print('''
            When I originally started to learn about Pandas and look at a
        project to do I found a data set about police shootings. There was
        a lot of data and I felt that I did not have the skills to work
        on it at the time. I put off the project and spent my time working
        on numerous other projects.
            I have come back to police shooting project. I found data, from
        the Washington Post on Kaggle. I decided to look at the data and see
        if I could find anything interesting. Before I mention some of the quick
        conclusions that I found, I would like to explain a little bit about
        me.
            I served in the Marine Corps for 8 years-2000-2008. During that time
        I was deployed to Iraq and Afghanistan. It was also during those
        8 years that I read heavily about insurgencies and how to fight them.
        The one strategy, which must be used, to fight an insurgency is to
        build trust with the people. If trust is not gained then the
        insurgency will eventually win.
        ''')
        input('Press enter to continue to read ')
        print('\033c')
        print('''
            A police department must build trust with the people it is meant to
        serve and protect. At this point, I would like to state that I consider
        myself a little right of center. I also believe in the military as an
        institution. Ever since I was little I followed the rules and was very
        disciplined. Up to this point in my life, I have only had a handful
        of encounters with the police. All of them, except for one, I have to
        say were rather 'intimidating'. They seemed focused on lecturing me
        rather than to be helping.
            Maybe it came from watching to many cartoons were police are helpful
        and nice, when I was a little, that I got my impression of how police
        are supposed to act. Now, those experiences that I had with police were
        not bad. They just could have been a lot nicer and friendlier.
            If this is my experience with police, an individual who left the
        Marines as a Captain, who is middle class and white than I can only
        imagine what other races must experience. The fact of the matter is that
        police should always be gaining the trust of the population they are
        meant to serve and protect. The moment that lethal force is used the
        police will start losing trust in the community. At this point, I will
        stop my reflection here and dive into the data. 
        ''')
        input('Press enter to continue to read ')
        print('\033c')
        print('''

        ''')
        input('Press enter to continue ')

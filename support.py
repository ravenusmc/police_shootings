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
        print('\033c')
        print('''
            Saying all of that, I want to now mention that this data comes from
        the Washington Post. The post on Kaggle has the following information:
        "In 2015, The Post began tracking more than a dozen details about each
        killing — including the race of the deceased, the circumstances of the
        shooting, whether the person was armed and whether the victim was
        experiencing a mental-health crisis — by culling local news reports,
        law enforcement websites and social media and by monitoring independent
        databases such as Killed by Police and Fatal Encounters.
            The Post is documenting only those shootings in which a police
        officer, in the line of duty, shot and killed a civilian — the
        circumstances that most closely parallel the 2014 killing of Michael
        Brown in Ferguson, Missouri, which began the protest movement
        culminating in Black Lives Matter and an increased focus on police
        accountability nationwide. The Post is not tracking deaths of people in
        police custody, fatal shootings by off-duty officers or non-shooting
        deaths."
        ''')
        input('Press enter to continue ')
        print('\033c')
        print('''
            I had heard of the Washington Post and possibly the Guardian,
        tracking deaths by police. I also knew that their data is probably not
        complete since there is no law requiring the police to report when
        they have killed someone. Thus, the data that will be examined in this
        program, may/is probably incomplete. Please be aware of that when
        using the program.
        ''')
        input('Press enter to continue ')

    #This method will show the user some of the conclusions that I have drawn
    #from this project. I really should have called a file for this method.
    #This, I believe, is not the way to do things in a project!
    def conclusion(self):
        print('\033c')
        print('''
                To start, in the readme file of this project is more resources
            that I used to build this project. I think that one lesson that I
            at least learned from building this project is that African
            Americans only make up 14 percent of the U.S. population but they
            are 25 percent of the deaths by police. This number, more than
            anything, tells me that there are some biases due to
            social/economical/racial factors.
                At this point, I will say that personally I believe that police
            should fully know the neighborhoods they patrol. In the neighborhood
            that I live in, there are at least two cops. However, I have never
            spoken with them once. They should be out, walking around, talking
            to people. Building a sense of connection between themselves and the
            communities that they serve.
        ''')
        input('Press enter to continue to read ')
        print('\033c')
        print('''
                I want to make the point that in building this project I
            knew that I would offend either people who support the police or
            those who are against them. This may be the case and it is a risk
            that I am taking. Again, the main goal of this project was to
            continue working on my skills with Pandas.
                The final point that I would like to make is about a thought
            that continues to huant me. I served in Iraq, at Camp Fallujah,
            from August of 2006 to March of 2007. I was a 1st Lt there and had a
            platoon of roughly 40 Marines. We were told, on a daily basis, that
            if any of my Marines fired a weapon at an Iraqi there would be an
            investigation and depending on how that turned out, possibly
            jail time for the Marine. Why is that in Iraq, killing an Iraqi,
            seemed to bring upon such heavy consequences compared to a police
            officer killing a U.S. citizen here in the U.S?
        ''')
        input('Press enter to continue to main menu ')

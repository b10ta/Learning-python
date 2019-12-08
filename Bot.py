import os
from datetime import date
import pprint
import time


def topics_number(x):
    size = len(x)
    for i in range(size):
        print(i+1, x[i])


def goodBye():
    if True:
        print('Good Bye Freind')
        return 0


os.system('clear')
print("Today's date:", date.today())
print('welcome to this small Bot project')
print('Hello! , What should we call you \'_\' >>')
name = input()
topics = ['Sport', 'Movies', 'Programming']
if name.isalpha():
    print('Nice to meet you  ' + name)
    time.sleep(2)
    print("WHich topic do you like to talk about \n this our List : ")
    time.sleep(2)
    print(topics_number(topics))
    time.sleep(3)
    print('Are you intersted in our Topics Yes/No')
    answer = input()
    if answer.isalpha():
        if answer.lower() == 'yes':
            print(topics_number(topics))
            time.sleep(2)
            print('Choose Carfully a number Lol 1-3')
            number = input()
            if number.isdecimal and number == '1':
                print('Let me guess you like Football')
                bot_answer = input()
                if bot_answer.lower() == 'yes':
                    print('Wow i can read people Mind LOL')
                    time.sleep(1)
                    print('So let me guess which country is your favorite Team')
                    country = ['Spain', 'England',
                               'France', 'Germany', 'Others']
                    time.sleep(2)
                    print(topics_number(country))
                    country_choise = input()
                    time.sleep(1)
                    if country_choise.isdecimal and number == '1':
                        print(
                            ' Must be Barcalona or Real-Madrid \n Ok let me Tell you one thing Barcalona is the Best Lol')
                        time.sleep(2)
                        goodBye()
                    if country_choise.isdecimal == 2:
                        print(' wOW England i will go for Liverpool ')
                        time.sleep(2)
                        goodBye()
                    if country_choise == 3:
                        print(
                            'if you dont live in France it must Be Paris Saint-Germain')
                        time.sleep(2)
                        goodBye()
                    if country_choise == 4:
                        print(' Germany :i will go for Dortmund ')
                        time.sleep(2)
                        goodBye()
                    if country_choise == 5:
                        print(
                            'i think will be not easy to guees the teams in other countries ')
                        time.sleep(2)
                        goodBye()
                else:
                    print(' I knew it im bad at reading peopel mind')
                    time.sleep(2)
                    goodBye()
            elif number.isdecimal and number == '2':
                print('One of my Favor Topics *_* \ntell me about ur favorite Movies')
                Movies_List = []
                Movies_List = input()
                bot_List = ['Mr.Robot', 'Wohami', 'Inception', 'Joker', ]
                print('intersting List i will watch it once >>>' + Movies_List)
                time.sleep(2)
                print('Maybe you can Look at my Movies List')
                time.sleep(2)
                print(','.join(bot_List))
            elif number.isdecimal and number == '3':
                print(
                    'Programming ..................... Yepppp \n tell me about your favorite Language')
                programming = str(input())
                time.sleep(1)
                if programming.lower() == 'python ':
                    print('wow my favorite also')
                    time.sleep(2)
                    goodBye()
                else:
                    print('i didnt expect ' + programming +
                          ' is your favorite languge')
            else:
                print('Enter a number next time ')

else:
    print("Please enter Letters ")

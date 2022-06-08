import os
import random
import string
from termcolor import cprint, colored

settings = {
    'lower' : True,
    'upper' : True,
    'symbol' : True,
    'number' : True,
    'space' : False,
    'length' : 8
}

PASS_MAX_LENGTH = 20
PASS_MIN_LENGTH = 4

def clear_screen():
    os.system('clear')

# def welcome():
#     print('** Welcome to Randoom Password Generator **')
 
def get_yes_or_no_for_settings(option, default):
  
    while True:
            user_input = input(f'Include {option} ? / [ Default is: {default} ] || ( y: Yes , n: No , Enter: Default ): ')
            print()
            if user_input == '':
                return default

            if user_input in ['y', 'n']:
                return user_input == 'y'

            cprint('Invalid input.Please try Again.', 'red')    
 

def get_user_password_length(option, default, pw_min_length = PASS_MIN_LENGTH, pw_max_length = PASS_MAX_LENGTH):

    while True:
        user_input = input(f'Enter Pasword Length ? / [ Default is: {default} ] || ( Enter: Default ): ')
        

        if user_input == '':
            return default

        if user_input.isdigit():
            user_password_length = int(user_input)
            if PASS_MIN_LENGTH <= user_password_length <= PASS_MAX_LENGTH:
                return user_password_length
            cprint('Invalid input.', 'red')
            cprint(f'Password Length should be between {PW_MIN_LENGTH} and {PW_MAX_LENGTH}.', 'red')
        else:
            cprint('Invalid input. You should enter a number.', 'red')

        cprint('Please try again.', 'red')


def get_settings_from_user(settings):

    for option, default in settings.items():
        if option != 'length':
            user_choice = get_yes_or_no_for_settings(option, default)
            settings[option] = user_choice
        else:
            user_password_length = get_user_password_length(option, default)
            settings[option] = user_password_length


def ask_if_change_settings(settings):
    cprint('** Welcome to Randoom Password Generator **\n', 'yellow')
    while True:
        print(settings, '\n')
        user_answer = input('Do you want to change default settings? ( y: Yes , n: No , enter: Yes ): ')
        if user_answer in ['y', 'n', '']:
            if user_answer in ['y', '']:
                print()
                print('-' * 5, 'Change Settings', '-' * 5)
                print()
                get_settings_from_user(settings)
            break
        else:
            cprint('Invalid input.', 'red')    
            cprint('Please try again.', 'red')
        

def generate_random_char(choices):

    choice = random.choice(choices)
    if choice == 'lower':
        return random.choice(string.ascii_lowercase)
    if choice == 'upper':
        return random.choice(string.ascii_uppercase)
    if choice == 'number':
        return random.choice(string.digits)
    if choice == 'symbol':
        return random.choice(string.punctuation)
    if choice == 'space':
        return ' '
 

def password_generator(settings):
    final_password = ''  
    password_length = settings['length']     

    choices = list(filter(lambda x : settings[x] == True, ['lower', 'upper', 'number', 'symbol', 'space']))

    for i in range(password_length):
        final_password += generate_random_char(choices)

    return final_password


def password_generator_loop(settings):
    while True:
        cprint('-' * 30, 'cyan')
        cprint(f'Generated Password : {password_generator(settings)}', 'green')

        while True:
            another_password = input('\nDo you want another password ? / ( y: Yes , n: No , enter: Yes ):')
            if another_password in ['y', 'n', '']:
                if another_password == 'n':
                    return
                break
            else:
                cprint('Invalid input.'' Choose from:( y: Yes , n: No , enter: Yes )', 'red')
                cprint('Please try again.', 'red')
            

def run():
    clear_screen()
    ask_if_change_settings(settings)
    password_generator_loop(settings)
    cprint('\n * Thank You * \n', 'cyan')


run()
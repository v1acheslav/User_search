#!/usr/bin/python3

user_list = dict(Slava = '096-895-44-55', Alex = '097-777-74-74')
def action_request():
    request = input('''
    Do you wish to create a new user or find an existing?:
    Please enter 1 to create a new user or 2 to find an existing user.    
    ''')
    request_result = check_input((request).replace(' ', ''))
    while not request_result:
        print('Only numbers are allowed! Please enter 1 to create a new user or 2 to find an existing user')
        request = input('''
            Do you wish to create a new user or find an existing?:
            Please enter 1 to create a new user or 2 to find an existing user.
            ''')
        request_result = check_input((request).replace(' ', ''))
    if request_result == '1':
        user_add()
    elif request_result == '2':
        user_search()
def check_input(input_data):
    input_data = str(input_data)
    # Check the basics
    if len(input_data) > 1:
        print('len is more than 1')
        return False
    # Check if we are getting passed correct characters
    for character in input_data:
        if character not in ['1','2']:
            print('{} not in allowed range'.format(character))
            return False
    return input_data
def user_add():
    new_user = input('Please enter your name:')
    user_number = input('Please enter your number:')
    if user_list.get(new_user) == None:
        user_list[new_user] = user_number
        print(user_list)
    else:
        print('The entered user {} is already in the list'.format(new_user))
def user_search():
    entered_user = input('Please enter a user name:')
    if user_list.get(entered_user) != None:
        print(user_list.get(entered_user))
    else:
        print('The user is not in our list')
action_request()
while True:
    request_again = input('''
        Do you want to repeat operation?
        Please type Y for YES or N for NO.
        ''')
    if request_again.upper() == 'Y':
        action_request()
    elif request_again.upper() == 'N':
        print('See you later.')
        break
    else:
        continue

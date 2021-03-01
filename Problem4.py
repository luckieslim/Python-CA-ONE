# Problem 4
# Implement the MYPY Phone Book System in Python which allows users to add, delete, update and
# lookup phone numbers. 
# The MYPY Phone Book System should store the individual’s Full Name and Phone Number.
# Your program should not allow users to add the same number twice.
# On adding, deleting, updating or looking up a number, your program should let the user know
# if the operation was successful or not. 
# On looking up a number return the full name and number of the individual; if the number is
# not found give the user the option to add the details they are looking up.
# The user can perform multiple actions; they can add a new entry and subsequently delete an
# entry without having to stop and start the program until they decide to quit.

phone_book = {} #Creating an empty dictionary where the phone numbers and names will be stored
while True:#to keep the program runing
    print('################################')
    print('MYPY PHONE BOOK')
    print('################################')
    print('1 : Add new Entry')
    print('2 : Delete Entry')
    print('3 : Update Entry')
    print('4 : Lookup Number')
    print('5 : QUIT')
    while True:#The loop will countinue if the user doesnt enter a valid input
        try:
             entry = int(input('Enter your entry: '))#asking the user to input any menu option
             break
        except:
            print('Enter a valid number. \n')# This error message will be displayed if the user doesnt input the right value


    if entry >= 1 and entry <= 5:# checking if the menu option inputed by the user is valid
        if entry == 1:#checking if the menu option is 1
            while True:#The loop will countinue if the user doesnt enter a valid input
                try:
                    phone_num = int(input('Enter phone number: '))# asking the user to input the phone number
                    break
                except:
                    print('Enter a valid number. \n')# This error message will be displayed if the user doesnt input the right value

            if phone_num not in phone_book.keys():#checking if the phone number inputed by the user already exist in the phonebook
                while True:#The loop will countinue if the user doesnt enter a valid input
                    try:
                      name =  input('Enter name: ')# asking the user to input the name
                      break
                    except:
                      print('Enter a valid name. \n')# This error message will be displayed if the user doesnt input the right value

                phone_book.update({phone_num : name})#adding the phone number and name to the phonebook
                print('Number added successful. \n')
            else:
                print('Number already exist. \n')#this error message will display if the number already exist


        if entry == 2:#checking if the menu option is 2
            while True:#The loop will countinue if the user doesnt enter a valid input
                try:
                    phone_num = int(input('enter phone number: '))#asking the user for the phone number
                    break
                except:
                    print('Enter a valid number. \n')# This error message will be displayed if the user doesnt input the right value

            if phone_num in phone_book.keys():#checking if the phone number inputed by the user already exist in the phonebook
               # del_num = phone_book.pop(phone_num)
               del phone_book[phone_num]# delete the phone number from the phone book
               print(phone_num, 'has been deleted successfully. \n')
              
            else:
                print('Number does not exist.\n')


        if entry == 3:#checking if the menu option is 2
            for key, value in phone_book.items():#getting the phone number and names in the phonebook
                print(key, value)# print out the phone number and names in the phonebooh
            while True:#The loop will countinue if the user doesnt enter a valid input
                try:
                    phone_num = int(input('Enter phone number: '))#asking the user for the phone number
                    break
                except:
                    print('Enter a valid number. \n')# This error message will be displayed if the user doesnt input the right value

            if phone_num in phone_book.keys():#checking if the number is in the phonebook
                while True:#The loop will countinue if the user doesnt enter a valid input
                    try:
                         new_phone_num = int(input('Update phone number: '))#asking the user to update the phone number
                         break
                    except:
                         print('Enter a valid number.\n')# This error message will be displayed if the user doesnt input the right value
                while True:#The loop will countinue if the user doesnt enter a valid input
                    try:
                        name = input('Update name: ')#asking the user to update the name
                        break
                    except:
                        print('Enter a valid name. \n')# This error message will be displayed if the user doesnt input the right value

                phone_book.pop(phone_num)# deleting the selected phone number from the phone book
                phone_book.update({new_phone_num: name})#updating the phonebook
                print('Update successful. \n')

            else:
                print('Number not found. \n')


        if entry == 4:#checking if the menu option is 2
            while True:#The loop will countinue if the user doesnt enter a valid input
                try:
                    phone_num = int(input('Enter phone number: '))#asking the user for the phone number
                    break
                except:
                    print('Enter a valid number. \n')# This error message will be displayed if the user doesnt input the right value

            if phone_num in phone_book.keys():#checking if the number is in the phonebook
               print(phone_num, phone_book[phone_num])#printing the number and name
            elif phone_num not in phone_book:#checking if the number is in the phonebook
                while True:#The loop will countinue if the user doesnt enter a valid input
                    try:
                        option = input('Number not found \n Do you want to add this number (yes/no):  ')#asking the user to save the number or not
                        break
                    except:
                        print('Enter a valid input. \n')# This error message will be displayed if the user doesnt input the right value

                if option.lower() == 'yes':#checking the input of the user
                    while True:#The loop will countinue if the user doesnt enter a valid input
                        try:
                             name = input('Enter name: ')#asking the user to input the name
                             break
                        except:
                            print('Enter a valid name. \n')# This error message will be displayed if the user doesnt input the right value

                    phone_book.update({phone_num : name})#updating the phonebook
                    print('Number Added Successful')
                    print(phone_book,'\n')
                elif option.lower == 'no':#checking if the option is no
                    print('Number not added. \n')
                else:
                    print('Invalid Option, Enter (yes/no).\n')

        if entry == 5 :#checking the option 
           
            break

    else:
        print('invalid option. \n')# This error message will be displayed if the user doesnt input the right value



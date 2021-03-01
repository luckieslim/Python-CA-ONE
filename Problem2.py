# Problem 2
# Write a program in Python which prompts the user for their username in the format Domain Name\Username 
# On entering their domain and username and pressing carriage return, write out to the console window each individual data item
# NOTE: The user can enter any combination of domain and username.


print('###################################')
print('WELCOME TO THE DBS CONSOLE')
print('###################################')


#divider = "\\"
#sub = string.find('\\') 

#if divider in string:
#    domain = string[:sub]
#    sub += 1
#    username = string[sub:]
#    print('Domain :', domain)
#    print('Username :', username)
#else:
#    print('Incorrect syntax')


while True: #The loop will countinue if the user doesnt enter a valid input
    string = input('Please enter your username: ') #get input from the user

    try:
        username = string.split("\\", 1) # split a string into a list and using \ as the seperator
        domain = username[0] # storing the first value of the list 
        name = username[1] # storing the second value of the list
        break

    except:
        print("Invalid format") # This error message will be displayed if the user doesnt input the right format

print("\nDomain :", domain)
print("Username :", name)
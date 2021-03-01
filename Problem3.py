# Problem 3
# Write a program in Python that prompts the user to enter a number of integer values. 
# The program stores the integers, counts the frequency of each integer and displays the frequency

print('##########################')
print('WELCOME TO THE DBS CONSOLE')
print('###########################')

while True:#The loop will countinue if the user doesnt enter a valid input
    try:
        numlist = int(input('Input the number of element :')) #asking the user to input the lenght of the list
        break
    except:
        print('Invalid Number. \n')# This error message will be displayed if the user doesnt input the right value

print('Input', numlist, 'elements in the list :')

list = []

num = 0

while num < numlist:#checking if num is less than the lenght of the list
    while True:#The loop will countinue if the user doesnt enter a valid input
        try:
            element = int(input("element - "+ str(num) + " : " ))#asking the user to input the elements into the list and also displaying the index number at whicch the element will be stored at
            list.append(element)# adding the element to the list
            num += 1 #incrementing num
            break
        except:
             print('Invalid Number. \n')# This error message will be displayed if the user doesnt input the right value
def frequency_count() :# creating a function that will loop through the list without repitition and count the number of times each element occur
    dup = [] # creating an empty list where the elements without repitition will be stored
    for x in list:# checking each element in the first list
        if x not in dup:#checking if the element is already in the second list.
           dup.append(x)#will only add element that does not exist in second list
    for x in dup:#for each element in the second list the program will count how many times it occurrs in the first list
        frequency = list.count(x)#counting how many times it oocured
        print (x, 'occures',frequency, 'times')#printing each element without repitition and thier frequency

frequency_count()# calling the function frequency
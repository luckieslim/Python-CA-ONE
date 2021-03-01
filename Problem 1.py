# Problem 1
# Write a program in Python to prompt the user to input their
# name, employee number, week ending date, hours worked, rate per hour, standard and overtime tax percentage rate.
# Use the data input to calculate gross pay, tax deductions and net pay. 
# Output the results as a formatted payslip.
# Assume that a standard working week is 37.5 hours.
# E.g. Ask the user to enter the following data:
# Employee Name:            (sample input – Mark Bate)
# Employee Number:          (sample input – 123456789A)
# Week ending:              (sample input - 26/01/2018)
# Number of hours worked:   (sample input – 42.5)
# Hourly Rate:              (sample input – 10.50)
# Overtime Rate:            (time-and-a-half as 1.5)
# Standard Tax Rate:        (sample input – 20)
# Overtime Tax Rate:        (sample input – 50)
# 
# Once the above data has been entered the program should display the employee’s payslip as per the following example:
#
#                               PAYSLIP
# WEEK ENDING 26/01/2018
# Employee: Mark Bate
# Employee Number: 123456789A
#                               Earnings                    Deductions
#                               Hours   Rate    Total
# Hours (normal)                37.50   10.50   393.75      Tax @ 20%   78.75
# Hours (overtime)              5.00    15.75   78.75       Tax @ 50%   39.37
#
#                               Total pay:                             472.50
#                               Total deductions:                      118.12
#                               Net pay:                               354.38

#SOLUTION

import datetime #importing datetime libary for date manipulation

name = input('Enter Employee Name: ') # to get employee name

employee_number = input('Enter Employee Number: ')# to get employee number
while True:
    try:
        date_entry = input('Enter Your Week Ending Date in DD/MM/YYYY format: ')# get date for week ending
        day, month, year = map(int, date_entry.split('/'))# spliting the week ending date and assigning it to different variables
        week_ending_date = datetime.date(year, month, day)# using the datetime libary to format the entered week ending date
        break

    except:
        print('Type a valid date with the given fomat (DD/MM/YYYY). \n') # This error message will be displayed if the user doesnt input the right format
while True:
    try:
        hours_worked = float(input('Enter Your Hours Worked: '))# getting the hours worked from the user
        if hours_worked > 37.5 :#checkinh if the hours worked is greater than 37.5 to get the overtime 
            over_time = hours_worked - 37.5
            hours_worked = 37.5
        else:#if the hours worked is not greater than 37.5 then there is no overtime
            over_time = 0
        break

    except:
        print('Enter a valid value. \n') # This error message will be displayed if the user doesnt input the right format
while True:
    try:
        hourly_rate = float(input('Enter Your Rate per hour: '))# asking the user to input the rate per hour
        break

    except:
        print('Enter a valid input.\n') # This error message will be displayed if the user doesnt input the right format
while True:
    try:
        standard_tax = float(input('Enter Your standard tax: '))# asking the user to input the standard tax rate
        break

    except:
        print('Enter a valid input.\n') # This error message will be displayed if the user doesnt input the right format
while True:
    try:
        over_time_tax = float(input('Enter Your Over time tax rate: '))#asking the user to input the over time tax rate
        break

    except:
        print('Enter a valid input.\n') # This error message will be displayed if the user doesnt input the right format




over_time_rate = hourly_rate * 1.5 # tp get the overtime rate we multiply the normal hourly rate times 1.5

normal_hours = hourly_rate * hours_worked# to get the normal hours rate we multiply the hourly_rate times the hours worked

over_time_hours = over_time_rate * over_time# to get the overtime hours we multiply the over time rate times over time

standard_tax_rate = normal_hours *(standard_tax/100)#to get the standard tax rate  we multiply the normal hours with the percentage of the standard tax

overtime_tax_rate = over_time_hours * (over_time_tax/100)#to get the overtime tax rate we multiply the overtimes hours times the percentage of over time tax

total_pay = normal_hours + over_time_hours# to get the total pay we add both the normal hours and over time hours

total_deduction = standard_tax_rate + overtime_tax_rate# to get the total deduction we add both the standard tax rate and the over time tax rate

net_pay = total_pay - total_deduction# to get the net pay we subtract the the total deduction from the total pay

print('\n\t\t\t\t PAYSLIP')
print('WEEK ENDING:',week_ending_date.strftime("%d/%m/%Y"))#use to format the date time 
print('Employee:',name)
print('Employee Number:',employee_number)
print('\t\t\t Earning \t \t  Deduction')
print('\t\t\t Hours \t Rate \t total \t ')
print('Hours (normal) \t \t', str(round(hours_worked, 2)), '\t', str(round(hourly_rate, 2)), '\t', str(round(normal_hours, 2)),'  Tax @  ',str(round(standard_tax, 2)),'%  ', str(round(standard_tax_rate, 2)))
print('Hours (overtime) \t ', str(round(over_time, 2)), '\t', str(round(over_time_rate, 2)), '\t', str(round(over_time_hours, 2)),'  Tax @  ',str(round(over_time_tax, 2)),'%  ', str(round(overtime_tax_rate, 2)),'\n')
print('\t\t\t Toatl pay: \t \t \t\t', str(round(total_pay, 2)))
print('\t\t\t Total deductions: \t \t \t',str(round(total_deduction, 2)))
print('\t\t\t Net pay: \t \t  \t\t',str(round(net_pay, 2)))

#\n is used to print in a new line
#\t is used to give marginal space in between two words
#str(round(variable, 2)) function is used to round the number to two decimal places
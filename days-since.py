
from datetime import datetime, timedelta


user_input = input('Please enter a date in YY/MM/DD format: ')

#strptime method takes in a string and convert into a python date obj
user_input_date = datetime.strptime(user_input, '%Y/%m/%d')

#print('Your input is : ' + str(use_input_date))
#print('Today is: ' + datetime.today().strftime('%Y-%m-%d'))

delta = datetime.today() - user_input_date


print( "It's been " + str(delta.days) + ' days since ' + user_input)


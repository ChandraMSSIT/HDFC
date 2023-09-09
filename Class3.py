# Data types
# it represents type of data
# we have two types of data types => Primitive data types, Sequence data types
# Primitive data types
# String , int , float,bool
# Python is a dynamically typed language

# String
name = "python"
# how to check data type
# the data which is defined between quotes (it can be single or double) considered as string
print("checking type of name :",type(name))
address ='#23,BLR'
print("checking type of address :",type(address))

# if it is a multiline need to use 3 single quotes
story = '''hi m Online Python compiler (interpreter) to run Python online.
           Write Python 3 code in this online editor and run it '''

account ='34555556'

# String methods
print(name.upper())
name ='Python'
print(name.lower())
name ='hello'
print(name.capitalize())
name = 'Hello World'
print(name.swapcase())

#
name = 'PYTHOn'
print(name.isupper())
print(name.islower())
print(account.isdigit())
print(account.isalpha())
print('starts with',story.startswith('hello'))
print('contains ', 'online' in story)
# we will see integers
# Int

aadhar = 34556677767
print("check type of aadhar" ,type(aadhar))

# float

account_balance = 2344.44
print("type of accountbalance : ", type(account_balance))

# bool (boolean)
# it contains True or False
is_data_exists = False
print("type of is data exists ", type(is_data_exists))
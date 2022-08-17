# write a python code to check valid password or not 
# password should be at least 8 characters long and should contain at least one uppercase letter, one lowercase letter and one digit
# if the password is valid print "Valid Password" otherwise print "Invalid Password"


import re


def passwordchecker(password):
    if len(password) < 8 or len(password) > 16:
        print("Invalid Password")
    elif not re.search("[a-z]", password):
        print("Invalid Password")
    elif not re.search("[A-Z]", password):
        print("Invalid Password")
    elif not re.search("[0-9]", password):
        print("Invalid Password")
    else:
        print("Valid Password")

passwordchecker('SamirS123')




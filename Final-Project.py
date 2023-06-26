
#!/bin/python3

#Final Project CYB333 Password Complexity Requirements

import re

def pwcheck(password):      #defining 'pwcheck' as a process to take argument of password and validate the requirments
    
    if len(password) >= 10:
        return False        #Test to ensure PW is at greater than or equal to 10 characters

    if not re.search(r'[A-Z]', password):
        return False        #Test to ensure password contains at least one uppercase letter

    if not re.search(r'[a-z]', password):
        return False        #Test to ensure password contains at least one lowercase letter

    if not re.search(r'[!@#$%^&*(),./<>?[]{}]', password):
        return False        #Test to ensure password contains at least one special character

    return True             #If code progresses this far without returning false, a True will be returned

password = input("Please read complexity requirements and type in password: ") #Queries user for proposed password

validpw = pwcheck(password)                                                    

if validpw:
    print("Password Created Successfully")
else:
    print("INVALID: Please Check Complexity Requirements and Try Again.")
#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen):
    #
    #
    characters = string.ascii_letters + string.digits + string.punctuation
    print(characters)
    password = ""
    for i in range(passLen):
        password = password + random.choice(characters)    
    #

    return password

def InitPasswordLen():
    len=int(input("Introducir longitud: "))
    result=RandomPasswordGenerator(len)
    print(result)

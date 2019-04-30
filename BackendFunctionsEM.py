# -*- coding: utf-8 -*-
"""
Spyder Editor
@author: Philip Irving

This is file works with the front end Gui build for the enigma machine.
Each key is set before the gui runs, to make any changes to the key must be done inside of this file 
"""
from EnigmaGuiEM import *

#Change the Keys t different integers
key1 = 11
key2 = 12
key3 = 13
key4 = 14
#True is Encrypting False is Decrypting
encrpt =  True


#print("Message:",theString,"\nKeys:",key1,key2,key3,key4,"\nWill you be Encrpting:",encrpt)

def EnigmaCipher(string, key):   #Func for ciphering 
    l = []
    l += string
    i = 0
    q = ""
#    print("Before:", string)    #For Debuging
    
    while i != len(string):
        #turn chr into assci value 
        e = ord(l[i])
        move = key % 10
        #shift assci vlaue by number
        e += move
        #turn assci value into chr 
        q += chr(e)
        #return e
        i += 1
#    print("After: ",q)      #For Debuging
    return q


def EnigmaDecripter(string, key):   #Func for decripting 
    l = []
    l += string
    i = 0
    q = ""
#    print("Before:", string) #For Debuging
    
    while i != len(string):
        #turn chr into assci value 
        e = ord(l[i])
        move = key % 10
        #shift assci vlaue by number 
        e -= move
        #turn assci value into chr 
        q += chr(e)
        #return e
        i += 1
#    print("After: ",q)      #For Debuging
    return q


def EngimaMachine(string):
    global key1
    global key2
    global key3
    global key4
    global encrpt
    
#    global theString
    if encrpt == True:      # For Encrpyting
        print("Encrypting Message....\n")
        string = EnigmaCipher(string, key1)
        string = EnigmaCipher(string, key2)
        string = EnigmaCipher(string, key3)                
        string = EnigmaCipher(string, key4)
        print("Done:",string,"\n")
        return string
        
    if encrpt == False:     # For Dercpyting
        print("Decrpyting Messsage....\n")
        string = EnigmaDecripter(string, key4)
        string = EnigmaDecripter(string, key3)
        string = EnigmaDecripter(string, key2)
        string = EnigmaDecripter(string, key1)
        print("Done:",string,"\n")
        return string
    
def convertStr(vari):
    splitstr = []
    intlist = []
    splitstr += vari
    

# Enigma-Machine

User story
---

This is a project I took on for a class about cryptography. I based this off of the Enigma machine used by Nazi germany during World War II.  
```gherkin=
Feature: Encrypting Function

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
```

```gherkin=
Feature: Decrypting Function

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
```

## Issues to resolve for the Future 
 
* Implement mutatabkle keys into the GUI window 

* Improve Encrypting/Decrypting functions



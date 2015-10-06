#97A - 122Z
Uinput = raw_input("input text here: ")
key = input("Int for the key: ")

cryp = ""
upper = bool

#the encrypting process
def crypt(a, b):
    new = ord(b) + a
    while new > 122:
        new -=26
    return new

#check if encrypt = True
for i in range(0, len(Uinput)):
    #is it a letter?
    if Uinput[i].isalpha():
        #Uppercase?
        if Uinput[i].isupper():
            upper = True
        #Lowercase?
        elif Uinput[i].islower():
            upper = False
        #UPPERCASE 
        if upper == True:
            cryp += str.upper(chr(crypt(key, Uinput[i])))
        #lowercase
        elif upper == False:
            cryp +=str.lower(chr(crypt(key, Uinput[i])))

       
print cryp










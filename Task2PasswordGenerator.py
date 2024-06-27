#Password Generator
import random
import string


print("    -------------PASSWORD GENERATOR-------------")
print("________________________________________________________________")

length=int(input("Enter the length of the password: "))

print('''Choose character set for password from these :
    1 . Digits
    2 . Letters
    3 . Special Characters
    4 . Exit''')


characterlist=""

while(True):
    choice=int(input("select a number: "))
    if (choice==1):
        characterlist+=string.digits
    elif(choice==2):
        characterlist+=string.ascii_letters
    elif(choice==3):
        characterlist+=string.punctuation
    elif(choice==4):
        break
    else:
        print("Please select a valid option: ")

password=[]
for i in range(length):
    randomchar=random.choice(characterlist)

    password.append(randomchar)

print("The Random password is "+"".join(password))
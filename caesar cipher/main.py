from encryptDecrypt import *

def menu():
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit the program")
    userInput = int(input("Enter : "))
    if (userInput):
        if (userInput == 1):
            encrypt()
            menu()
        elif (userInput == 2):
            decrypt()
            menu()
        elif (userInput == 3):
            exit()
        else:
            print("Please enter valid number")
            menu()

menu()


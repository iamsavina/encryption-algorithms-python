from .encryptDecrypt import encrypt

def menu():
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit the program")
    userInput = int(input("Enter : "))
    if (userInput):
        if (userInput == 1):
            encrypt()
        elif (userInput == 2):
            decrypt()
        elif (userInput == 3):
            exit()
        else:
            print("Please enter valid number")
            menu()


# def encrypt():
#     print("Ënter text to encrypt \n")
#     print("Running the program")

#     menu()

def decrypt():
    print("Decryptiong")
    print("Running the program")

    menu()

menu()
def encrypt():
    plaintext = input("Enter your cipher text : ")
    key = int(input("Please enter encryption key (1-25): "))
    print(plaintext,key)


    result = ""
    for i in range(len(plaintext)):
        
        char = plaintext[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
 
    print(result)

    

def decrypt():
    print("Decryptiong")
    print("Running the program")

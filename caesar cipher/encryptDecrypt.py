def encrypt():
    plaintext = input("Enter your plain text : ")
    key = int(input("Please enter encryption key (1-25): "))
    result = ""
    for i in range(len(plaintext)):
        
        char = plaintext[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
 
    return print("Your cipher text is : ",result)

    

def decrypt():
    plaintext = input("Enter your cipher text : ")
    key = int(input("Please enter encryption key (1-25): "))
    result = ""
    for i in range(len(plaintext)):
        
        char = plaintext[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            # result += chr((ord(char) + key-65) % 26 + 65)
            result += chr((ord(char) + key+65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            # result += chr((ord(char) + key - 97) % 26 + 97)
            result += chr((ord(char) + key + 97) % 26 + 97)
 
    return print("Your cipher text is : ",result)

import sys #sys is commonly used for system-related operations.

FIRST_CHAR_CODE=ord("A") #The ord function returns the Unicode code point of a character.
LAST_CHAR_CODE=ord("Z")
CHAR_RANGE=LAST_CHAR_CODE - FIRST_CHAR_CODE + 1 #It subtracts the Unicode code point of the first character from the Unicode code point of the last character and adds 1. 

def encrypt(message, k):
    result = ""
    for char in message.upper():#This method is used to convert all characters in the message to uppercase.
        if char.isalpha():#It is a method in Python used to check if the given character is an alphabetic character.
            char_code=ord(char) # The function returns the Unicode code point of the character char.
            new_char_code=char_code+k #The line calculates the new Unicode code point for the character after shifting by the specified key (k).

            if new_char_code>LAST_CHAR_CODE:#Basically,the code allows to start again from the beginning of the alphabet. 
                new_char_code-=CHAR_RANGE

            if new_char_code<FIRST_CHAR_CODE:#Basically, the code allows to move to the first aplhabet. 
                new_char_code+=CHAR_RANGE
        
            new_char=chr(new_char_code)
            result += new_char #it allows to append the character to the result string. 
    

        else:
            result+=char #if it is not alphabet, it will remains unchanged and is appended to the result string without any modification. 

    return result



def decrypt(message, k):
    return encrypt(message, -k)  # Decrypting is the same as encrypting with the negative key

if __name__ == "__main__":

    if len(sys.argv) != 3: #This condition checks if the number of command-line arguments is not equal to 3. 
        print("Usage: python caesar.py <word> <key>")
        sys.exit(1) #This line terminates the script with a status code of 1.

    
    message = sys.argv[1] # take in first arg as word
    
    key = int(sys.argv[2]) # take in second arg as int key

    encrypted = encrypt(message, key) # encrypt the word

    decrypted = decrypt(encrypted, key)  # decrypt the encrypted word

    print("Your original word is:", message)
    print("Your encrypted word is:", encrypted)
    print("Your decrypted word is:", decrypted)


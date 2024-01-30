import sys 

FIRST_CHAR_CODE=ord("A") 
LAST_CHAR_CODE=ord("Z")
CHAR_RANGE=LAST_CHAR_CODE - FIRST_CHAR_CODE + 1 #It subtracts the ASCII numeric values of the first character from the ASCII numeric values of the last character and adds 1. So 90-65+1=26, 26 is the char range. 26 represnets 26 alphabets.  

def encrypt(message, k):
    result = ""
    for char in message.upper():#This method is used to convert all characters in the message to uppercase.
        if char.isalpha():#It is a method in Python used to check if the given character is an alphabetic character.
            char_code=ord(char) # The function returns the ASCII numeric values of the character char.
            
            k = k % CHAR_RANGE # Use modulo operation to handle large keys. The Python modulo operator calculates the remainder of dividing two values. so the char range is 26, any number within 26 will be the same, however, any number that is larger than 26 will take for the reminder to ensure that k remaines the valid range for the Caesar cipher

            new_char_code=char_code+k #The line calculates the new ASCII numeric values for the character after shifting by the specified key (k).

            if new_char_code>LAST_CHAR_CODE:#Basically,the condition allows to start from the A to Z alphabet range. If new numberic value is larger than numercia value of Z (90), any new numberic value will minus 26 to ensure the number is within the 65 and 90 range so that letter can be within the range of alphabets.
                new_char_code-=CHAR_RANGE

            if new_char_code<FIRST_CHAR_CODE:#Basically,the condition allows to start from the A to Z alphabet range. If new numberic value is less than numercia value of A (65), any new numberic value will add 26 to ensure the number is within the 65 and 90 range so that letter can be within the range of alphabet.
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

    print("The original word is:", message)
    print("The encrypted word is:", encrypted)
    print("The decrypted word is:", decrypted)


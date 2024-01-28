import sys

FIRST_CHAR_CODE=ord("A")
LAST_CHAR_CODE=ord("Z")
CHAR_RANGE=LAST_CHAR_CODE - FIRST_CHAR_CODE + 1

def encrypt(message, k):
    result = ""
    for char in message.upper():
        if char.isalpha():
            char_code=ord(char)
            new_char_code=char_code+k

            if new_char_code>LAST_CHAR_CODE:
                new_char_code-=CHAR_RANGE

            if new_char_code<FIRST_CHAR_CODE:
                new_char_code+=CHAR_RANGE
        
            new_char=chr(new_char_code)
            result += new_char
    
        else:
            result+=char

    return result



def decrypt(message, k):
    return encrypt(message, -k)  # Decrypting is the same as encrypting with the negative key

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python caesar.py <word> <key>")
        sys.exit(1)

    # take in first arg as word
    message = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])

    # encrypt the word
    encrypted = encrypt(message, key)

    # decrypt the encrypted word
    decrypted = decrypt(encrypted, key)

    print("Your original word is:", message)
    print("Your encrypted word is:", encrypted)
    print("Your decrypted word is:", decrypted)


import sys

def encrypt(message, k):
    result = ""
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + k) % 26 + ord('A' if is_upper else 'a'))
            result += shifted_char
        else:
            result += char
    return result

def decrypt(message, k):
    return encrypt(message, -k)  # Decrypting is the same as encrypting with the negative key

if __name__ == "__main__":
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


# implementing ceaser cipher
def encryption(string, key):
    result = ""
    for i in string:
        if i.isupper():
            result += chr((ord(i) + key - 65) % 26 + 65)
        else:
            result += chr((ord(i) + key - 97) % 26 + 97)

    return result


def decryption(string, key):
    result = ""

    for i in string:
        if i.isspace():
            result += " "
        elif i.isupper():
            result += chr((ord(i) - key - 65) % 26 + 65)
        else:
            result += chr((ord(i) - key - 97) % 26 + 97)

    return result


string = input('Enter Message to encrypt: ').lower()
key = int(input('Enter key: '))

print(encryption(string, key))
print(decryption(encryption(string, key), key))

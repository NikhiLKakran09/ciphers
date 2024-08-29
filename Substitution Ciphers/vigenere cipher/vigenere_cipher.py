"""
    vignere cipher is a polyalphabetic cipher. It shifts each alphabet in the text to the position of the corresponding
    alphabet in the key.
"""

def encrypt(message : str, key : str) -> str:
    """
        return vigenere cipher
    """
    cipher= ''
    message = message.upper()
    key = key.upper()
    x = 0
    for i in range(len(message)):     
        if message[i].isalpha():
            cipher += chr((ord(message[i]) - 2 * ord('A') + ord(key[x % len(key)])) % 26 + ord('A'))
            x += 1
        elif message[i] == ' ':
            continue
        else:
            cipher += message[i]
    return cipher


def decrypt(cipher : str, key : str) -> str:
    """
        return decrypted message from vigenere cipher
    """
    message= ''
    cipher = cipher.upper()
    key = key.upper()
    x = 0
    for i in range(len(cipher)): 
        if cipher[i].isalpha():
            message += chr((ord(cipher[i]) - ord(key[x % len(key)])) % 26 + ord('A'))
            x += 1
        else:
            message += cipher[i]
    return message

if __name__ == '__main__':
    print("_____________________________________________________")
    print(" |                                                 |")
    print(" |                  Vigenere Cipher                |")
    print("_|_________________________________________________|_")
    key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        print("Current key: ",key)
        print("Choose one operation.")
        print("\t1)encode\t2)decode\t3)change key \t4)exit")
        try:
            choice = int(input(""))
        except:
            print("Wrong input format.")
            continue
        
        if choice == 1:
            text = input("Enter text to encode: \n>> ")
            print(f"Encoded text:\n {encrypt(text,key)}")
        elif choice == 2:
            text = input("Enter text to decode: \n>> ")
            print(f"Decoded text:\n {decrypt(text,key)}")
        elif choice == 3:
            key = input("Enter key string.\n >>")
            print("key changed.")
        elif choice == 4:
            print("Bye")
            break
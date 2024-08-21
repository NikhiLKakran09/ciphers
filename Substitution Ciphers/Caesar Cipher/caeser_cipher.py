# This code represent the working of caeser cipher in simple way.
import string

def encode(message: str, shift: int) -> int: 
    """ 
        This function takes text and substitution length as input and
        return cipher text as output.
        This function puts an alphabet at substitution length in the
        cipher text for each alphabet in text and rest of the characters and
        spaces are placed as it is.
    """

    cipher: str = ""
    for i in range(len(message)):
        char : chr = message[i]
        if char.islower():
            cipher += chr( (ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif char.isupper():
            cipher += chr( (ord(char) - ord('A') + shift)%26 + ord('A'))          
        else:
            cipher += char
    # cipher = cipher.replace(' ','')
    return cipher

def decode(message : str, shift : int) -> str:
    return encode(message,shift)


if __name__ == '__main__':
    print("_____________________________________________________")
    print(" |                                                 |")
    print(" |           Simple Caeser Cipher                  |")
    print("_|_________________________________________________|_")

    while True:
        print("Choose one operation.")
        print("\t1)encode\t2)decode\t9)exit")
        try:
            choice = int(input(""))
        except:
            print("Wrong input format.")
            continue
        if choice == 9:
            print("Bye")
            break
        elif choice == 1 or choice == 2:
            print("Enter text: ")
            text = input()
            print("Enter caeser shift number.")
            try:
                shift = int(input())
            except:
                print("Wrong input format. Retry again!")
                exit()
            
            if choice == 1:
                print("Encoded text:\n",encode(text,shift))
            elif choice == 2:
                print("Decoded text:\n",decode(text,shift))
            break
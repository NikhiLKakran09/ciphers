import string


def subst_dictx(shift: int) -> tuple:
    """
    Take a number as input and return tuple of two dictionaries: encoding and decoding
    """
    encoding : dict = {}
    decoding : dict= {}
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    for i in range(26):
        encoding[uppercase_letters[i]] = uppercase_letters[(i+shift) % 26]
        encoding[lowercase_letters[i]] = lowercase_letters[(i+shift) % 26]

        decoding[lowercase_letters[i]] = lowercase_letters[(i+shift) % 26]
        decoding[uppercase_letters[i]] = uppercase_letters[(i+shift) % 26]
    return encoding,decoding

def encode(message: str, subst: dict) -> str:
    return "".join('' if x == ' ' else subst.get(x,x) for x in message)

def decode(message: str, subst: dict) -> str:
    return encode(message,subst)

def print_string(subst):
    mapping = sorted(subst.items())
    alphabet = "".join(alpha for alpha,_ in mapping)
    cipher = "".join(ciph for _,ciph in mapping)
    return f"{alphabet}\n{cipher}"


def take_input(prompt):
    try:
        shift = int(input(prompt))
        return shift
    except:
        print("Wrong input format. Retry again!")
        exit()

if __name__ == '__main__':
    print("_____________________________________________________")
    print(" |                                                 |")
    print(" |                  Caeser Cipher                  |")
    print("_|_________________________________________________|_")
    shift = 1
    while True:
        encoding, decoding = subst_dictx(shift)
        print("Current Shift: ",shift)
        print("Choose one operation.")
        print("\t1)encode\t2)decode\t3)show encoding/decoding table\t4)change shift \t5)exit")
        try:
            choice = int(input(""))
        except:
            print("Wrong input format.")
            continue
        
        if choice == 1:
            text = input("Enter text to encode: \n>> ")
            print(f"Encoded text:\n {encode(text,encoding)}")
        elif choice == 2:
            text = input("Enter text to decode: \n>> ")
            print(f"Decoded text:\n {decode(text,decoding)}")
        elif choice == 3:
            print(f"Encoding strings:\n{print_string(encoding)}")
            print(f"Decoding strings:\n{print_string(decoding)}")
        elif choice == 4:
            shift = take_input("Enter shift value.\n >>")
            encoding,decoding = subst_dictx(shift)
            print("Shift changed.")
            continue
        elif choice == 5:
            print("Bye")
            break
           

"""
    Try automating this.
    • Get a data structure containing a few thousand English words.
    • Create a program that takes in an encoded string, then try decoding it with all 25
    shift values.
    • Use the dictionary to try to automatically determine which shift is most likely.
    Because you have to deal with messages with no spaces, you can simply keep a count of how
    many dictionary words show up in the decoded output. Occasionally, one or two words might
    appear by accident, but the correct decoding should have significantly more hits.
"""
import os
import string
from caeser import decode,subst_dictx 

def read(path: str) -> list:
    """
        open file specified by path return list of words otherwise return None
    """
    
    try:
        with open(path, 'r') as wordlist:
            ls = wordlist.read()
            ls = list(ls.split('\n'))
        return ls    
    except Exception as e:
        print(e)
        return None

def decrypt_cipher(cipher: str):
    """
        Return orignal decoded text.
    """

    shift = 0       # shift value to decrypt message
    subst = {}      # dictionary to store current decoding table
    matches = {i:0 for i in range(1,26)}    # store shift value and corresponding count of words
    wordlist = read('english_words.txt')    # list of 3000 words mostly used in english
    if wordlist:       
        for i in range(1,26):                # count number of words matching for each shift
            _ , subst = subst_dictx(i)
            text = decode(cipher, subst)
            for word in wordlist:
                if word in text:
                    matches[i] += 1
        
        shift = int(max(matches, key=matches.get))      # decrypt message
        if shift > 0:
            _, subst = subst_dictx(shift)
            decoded_message = decode(cipher,subst)
            return decoded_message    
        else:
            print("Bye")
            exit()


if __name__ == "__main__":
    print("_____________________________________________________")
    print(" |                                                 |")
    print(" |            Break caeser cipher                  |")
    print("_|_________________________________________________|_")
    print("Enter text to decrypt:\n>>",end=" ")
    text = input()
    print(f"Decoded text: {decrypt_cipher(text)}")
    exit()



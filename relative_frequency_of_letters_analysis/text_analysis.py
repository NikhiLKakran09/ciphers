import os,string,json

punctuations = string.punctuation
alphabets = string.ascii_lowercase

def analyse(path: str) -> list:
    """
        print the probability of each alphabet in provided text
    """
    try:
        with open(path, 'r') as text:
            bigtxt = text.read()
        text = ''.join('' if w in punctuations or w == '\n' else w.lower() for w in bigtxt)
        text_length = len(bigtxt)
        alphabet_density = { alphabet:text.count(alphabet)/text_length for alphabet in alphabets }
        return alphabet_density   
    except Exception as e:
        print(e)
        return None

if __name__ == "__main__":
    alphabet_density = analyse('big.txt')
    if alphabet_density:
        with open('./letter_frequency.lst','w') as fp:
            json.dump(alphabet_density, fp)
            print("Results saved to 'letter_frequency.txt file.")  
    
import sys
import string

def caesar_cipher(text, shift, mode="encode"):
   
    if not all(char in string.ascii_letters + string.digits + string.punctuation + " " for char in text):
        raise Exception("The script does not support your language yet.")
    
    if mode == "decode":
        shift = -shift
    
    result = []
    for char in text:
        if char.isalpha():
            alphabet = string.ascii_lowercase if char.islower() else string.ascii_uppercase
            new_char = alphabet[(alphabet.index(char) + shift) % 26]
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

def main():
    if len(sys.argv) != 4:
        raise Exception("Usage: python3 caesar.py <encode|decode> <text> <shift>")
    
    mode = sys.argv[1].lower()
    if mode not in ["encode", "decode"]:
        raise Exception("Invalid mode. Use 'encode' or 'decode'.")
    
    text = sys.argv[2]
    try:
        shift = int(sys.argv[3])
    except ValueError:
        raise Exception("Shift must be an integer.")
    
    try:
        result = caesar_cipher(text, shift, mode)
        print(result)
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()

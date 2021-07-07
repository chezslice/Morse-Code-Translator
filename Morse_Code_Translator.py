MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def message_encryption(message):
    
    cipher_variable = ''
    # Checking the character inside the message.
    for character in message:
        if character != ' ':

            # Look up inside the dictionary and adds corresponding code.
            cipher_variable += MORSE_CODE_DICT[character] + ' '
        else:
            cipher_variable += ' '
    return cipher_variable

# Decrypt morse code to the english language.
def message_decryption(message):
    
    message += ' '
    decryption = ''
    text = ''

    for character in message:
        # Check the spaces.
        if (character != ' '):
            x = 0
            text += character
        else:
            x += 1
            if x == 2:
                decryption += ' '
            else:
                decryption += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(text)]
                text = ''
    return decryption

# Defining the main function, to print out the outcome of the message.
def main():
    message = "HELLO WORLD THIS IS CHEZSLICE"
    output = message_encryption(message.upper())
    print(output)
    message = ".--. -.-- - .... --- -.  -....- .--. .-. --- --. .-. .- -- "
    output = message_decryption(message)
    print(output)


if __name__ == '__main__':
   main()
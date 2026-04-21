import sys


MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----'}


def encrypt(message):
    result = ''
    for letter in message:
        if letter != ' ':
            result += MORSE_CODE_DICT[letter] + ' '
        else:
            result += '/'


def main():
    """Do a Morse Code code from a string
    Take alphanumeric characters and space
    Space : /
    Alphanumeric :  . - 
    Have to use a dictionary
    """
#        assert (len(sys.argv == 2)), "wrong number of arguments"
    try:
        message = sys.argv[1]
        assert isinstance(message, str), "the arguments are bad"
        result = encrypt(message.upper())
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()

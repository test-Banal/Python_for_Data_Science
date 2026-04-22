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
    return result


def main():
    """Do a Morse Code code from a string
    Take alphanumeric characters and space
    Space : /
    Alphanumeric - .
    Have to use a dictionary
    """
#        assert (len(sys.argv == 2)), "wrong number of arguments"
    try:
        # nbr arg
        assert len(sys.argv) == 2, \
            "the arguments are bad"
        message = sys.argv[1]
        # isinstance = check str, > 0 si vide
        assert len(sys.argv[1]) > 0 and isinstance(message, str), \
            "the arguments are bad"
        # caracteres non voulus
        assert \
            all(c.upper() in MORSE_CODE_DICT or c == ' ' for c in message), \
            "the arguments are bad"
        result = encrypt(message.upper())
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()


"""   try:
        if (len(sys.argv) == 2):
            message = sys.argv[1]
            assert isinstance(message, str), "the arguments are bad"
            result = encrypt(message.upper())
            print(result)
        else:
            print("wrong number")
    except AssertionError as e:
        print(f"AssertionError: {e}")


def main():
    try:
        assert len(sys.argv) == 2 or len(sys.argv[1] == 0), "Wrong number of
        arguments, expected 2 argument"
        if (len(sys.argv[1]) == 0):
            print("test nulle")
        message = sys.argv[1]
        assert isinstance(message, str), "The arguments are bad"
        result = encrypt(message.upper())
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except KeyError as e:
        print(f"Caractère non supporté : {e}")"""

# https://www.lexilogos.com/clavier/morse.htm

import sys


def Count_characters(text: str):
    num_upper = 0
    num_tot = 0
    num_lower = 0
    num_ponct = 0
    num_digit = 0
    num_space = 0
    for char in text:
        num_tot += 1
        if (char.isupper()):
            num_upper += 1
        elif (char.islower()):
            num_lower += 1
        elif (char.isdigit()):
            num_digit += 1
        elif (char.isspace()):
            num_space += 1
        else:
            num_ponct += 1        
    print(f"The text contains {num_tot} characters:\n{num_upper}"
          f" upper letters\n{num_lower} lower letters\n{num_ponct}"
          f" punctuation marks\n{num_space} spaces\n{num_digit} digits")
    return


def main():
    """Function which count number of characters, digits, upper and lower
    letters, function marks, and spaces in string. If wrong number of arguments
    print error message with : AssertionError
    """
    if (len(sys.argv) > 2):
        print("AssertionError: Wrong number of arguments")
        return
    elif (len(sys.argv) == 1):
        print("What is the text to count?")
        Count_characters(sys.stdin.read())
    else:
        Count_characters(sys.argv[1])
    return


if __name__ == '__main__':
    main()


# ressource : https://docs.python.org/fr/3/library/__main__.html
# ressource : https://www.w3schools.com/python/python_user_input.asp
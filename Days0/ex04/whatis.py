import sys

if len(sys.argv) != 2:
    print("AssertionError: more than one argument is provided")
else:
    try:
        num = int(sys.argv[1])
        result = num % 2
        if (result == 0):
            print("I'm Even")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")

# ressources : https://koor.fr/Python/CodeSamples/SysArgv.wp
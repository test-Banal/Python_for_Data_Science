import ft_filter
import sys


def main():
    """Program to filter elements with a condition. A partir d'une string S
    et d'un entier N
    """
    if (len(sys.argv) != 3):
        print("AssertionError: the arguments are bad")
    else:
        list_S = sys.argv[1]
        if (isinstance(list_S, str) == 1):
            print("Error type argument")
        int_N = sys.argv[2]
        num_N = int(int_N)
        if (type(num_N) is not int):
            print("Error type argument")
        list_sf = list_S.split()
        ft_filter(list, int_N)
    return


if __name__ == '__main__':
    main()


# ressource : https://csatlas.com/python-import-file-module/
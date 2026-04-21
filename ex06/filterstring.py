from ft_filter import ft_filter
import sys

# Filtering function
def is_sup_four(word):
    """Function to check if str > 4, cf subject"""
    return len(word) > 4

def main():
    """Program to filter elements with a condition. 
    A partir d'une string S et d'un entier N.
    """
    try :
        if (len(sys.argv) == 3):
            list_S = sys.argv[1]
            int_N = sys.argv[2]
            num_N = int(int_N)
            if (type(num_N) is not int):
                print("Error type argument")
            list_sf = list_S.split()
            ft_filter(is_sup_four(), list_sf)
            
    except:
        
        
    return 


if __name__ == '__main__':
    main()


# ressource : https://csatlas.com/python-import-file-module/
# ressource : https://realpython.com/python-filter-function/#coding-with-pythonic-styleexi
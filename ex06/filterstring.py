import sys
from ft_filter import ft_filter


def main():
    """Filter words from a string that are longer than a given integer N."""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        list_S = sys.argv[1]
        int_N = sys.argv[2]
        assert isinstance(list_S, str) and int_N.lstrip('-').isdigit(), \
            "the arguments are bad"
        num_N = int(int_N)
        list_sf = list_S.split()
        result = ft_filter(lambda x: len(x) > num_N, list_sf)
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
# ressource : https://csatlas.com/python-import-file-module/
# ressource : https://realpython.com/python-filter-function/#coding-with-pythonic-styleexi
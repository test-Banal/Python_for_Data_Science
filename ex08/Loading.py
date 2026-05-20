import os
from typing import Generator


def ft_tqdm(lst: range) -> Generator[int, None, None]:
    """
        Re-implementation of tqdm progress bar using yield
    """
    total = len(lst)
    term_size = os.get_terminal_size().columns
    bar_size = term_size - 30

    for i, elem in enumerate(lst, 1):
        percent = int(i / total * 100)
        filled = int(bar_size * i / total)
        bar = "=" * max(0, filled - 1) + ">"
        bar = bar.ljust(bar_size)

        print(f"\r{percent:3}%|[{bar}]| {i}/{total}", end="")
        yield elem


# def main():
#    ft_tqdm()


# if __name__ == "__main__":
#    main()

# You can use get_terminal_size to adapt to the size of your terminal.

# https://stackoverflow.com/questions/76297644/implementing-tqdm-using-only-standard-python-library
# https://www.datacamp.com/tutorial/tqdm-python
# https://denishulo.developpez.com/tutoriels/python/barre-progression/
# https://blog.stephane-robert.info/docs/developper/programmation/python/generateurs/

# format temps necessitera une fonction
# yield
# /r revient debut de la ligne, permet d'ecraser la ligne precedente
# = mis ajour de la barre de chargement

# https://believemy.com/fr/glossaires/python/yield
# Generator[TypeYield, TypeSend, TypeReturn] -> Generator[int, None, None]:
# https://www.tresfacile.net/la-methode-de-chaine-de-caracteres-ljust-python/
# # pour ljust complete la bar d'espace
# █
# https://www.docstring.fr/glossaire/enumerate/ 
def ft_filter(funct, iterable) -> list:
    """ Reimplementation of built-in filter() using list comprehension.
    Returns elements of iterable for which funct returns True, or truthy
    elements if funct is None."""
    if funct is None:
        return [i for i in iterable if i]
    return [i for i in iterable if funct(i)]

# ressource : https://gayerie.dev/docs/python/python3/list_comprehension.html

# ressource : https://medium.com/norsys-octogone/exploration-de-python-
# traitement-des-s%C3%A9quences-avec-un-style-fonctionnel-filter-4da4d9ae6367

# ressource : https://www.datacamp.com/fr/tutorial/python-filter

# function is None: Si aps de fonction fournie garde les elements truth)


''' Ici avec une boucle for et pas une liste comprehension
def ft_filter(funct, *iterable) -> list:
    result = []
    for i in iterable:
        if funct is None:
            if i:
                result.append(i)
        else:
            if funct(i):
                result.append(i)
    return (result)
'''

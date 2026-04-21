def ft_filter(funct, iterable) -> list:
    if funct is None:
        return [i for i in iterable if i]
    return [i for i in iterable if funct(i)]

# ressource : https://gayerie.dev/docs/python/python3/list_comprehension.html

# ressource : https://medium.com/norsys-octogone/exploration-de-python-
# traitement-des-s%C3%A9quences-avec-un-style-fonctionnel-filter-4da4d9ae6367

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

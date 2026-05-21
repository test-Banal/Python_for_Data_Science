import math


def NULL_not_found(object: any) -> int:

    if (object is None):
        print(f"Nothing: {object} {type(object)}")

    elif (isinstance(object, float) and math.isnan(object)):
        print(f"Cheese: {object} {type(object)}")
    
    elif (isinstance(object, bool)):
        print(f"Fake: {object} {type(object)}")

    elif (object == 0 and type(object) is int):
        print(f"Zero: {object} {type(object)}")

    elif (object == ""):
        print(f"Empty: {type(object)}")

    else:
        print("Type not Found")
        return 1
    return 0

# Ressources :
# https://ladatascience.fr/2023/09/25/tester-variable-none-python
# https://stackoverflow.com/questions/944700/how-to-check-for-nan-values
# https://courspython.com/types.html
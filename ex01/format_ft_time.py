import time
from datetime import datetime

# time
current_timestamp  = time.time()
print(f"Seconds since January 1, 1970: {current_timestamp:,.4f} or {current_timestamp:.2e} in scientific notation")

# date
dttime = datetime.fromtimestamp(current_timestamp)
date_format = dttime.strftime("%b %d %Y")
print(date_format)


# Ressources :
# notation scientifique : https://ladatascience.fr/2023/02/07/utiliser-la-notation-scientifique-en-python/
# heure depuis 01/01/1970 : https://labex.io/fr/tutorials/python-how-to-get-system-time-in-python-435418
# date : https://docs.python.org/fr/3.7/library/datetime.html
# %b mois abrege, %d jour sur deux chiffres, %Y anne sur 4 chiffres
# fromtimestamp = converti nmbr en second en date et heure

# from datetime import datetime
# date = datetime.now().strftime("%b %d %Y" )
# print(date)
# First package

Objectif : creer premier package Python installable comme une vraie librairie.
-> installable avec : pip
-> apparaitre dans pip list
-> etre inspectable avec pip show -v
-> etre utilisable depuis n'importe ou dans le systeme

Rappel : un package est un dossier avec du code que tu peux importer partout, comme numpy, pandas... En gros re-utilisation du code sans copier coller.

En gros : modulaire -> reutilisable, meilleur organisation et facilite la maintenance.

## Installation

Dans bash, build : 
> python -m build

Checker si bien build :
> ls dist

Puis installer package comme dans le sujet : 
> pip install ./dist/ft_package-0.0.1.tar.gz
ou
> pip install ./dist/ft_package-0.0.1-py3-none-any.whl

## Test

Verifier avec la commande suivante :
> pip show -v ft_package

Et effectuer le meme test qu'ennonce dans le sujet :
> pip show -v ft_package

## Supprimer

Pour supprimer et desinstaller : 
> rm -rf dist build *.egg-info
> pip uninstall ft_package
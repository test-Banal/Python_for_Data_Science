ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#list
ft_list[1] = "World!"

#tuple
tmp_list = list(ft_tuple) #soit manuellement soit comme ici, en passant par une liste
tmp_list[1] = "France!"
ft_tuple = tuple(tmp_list)

#set
ft_set.discard('tutu!') #supprime puis ajoute nouveau element
ft_set.add('Paris!')

#dict
ft_dict["Hello"] = "42Paris!" 


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

#Ressources : https://courspython.com/index.html
#list : https://numerique.ostralo.net/python_AideMemoire/06b_Listes.htm
#tuple :https://www.google.com/search?client=ubuntu&channel=fs&q=comment+on+remplace+un+tuple+python
#set : https://www.docstring.fr/glossaire/sets/
#discard & add :  méthodes natives des objets Python, pas de fonctions externe ou specifique
#dict :https://koor.fr/Python/Tutorial/python_type_dict.wp
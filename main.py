liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
trois_premiers = liste[0:3]
trois_derniers = liste[-3:]
milieu = liste[1:-1]
premier_dernier = liste[::len(liste)-1]
#print(trois_premiers, trois_derniers,milieu,premier_dernier)

Index=liste.index("Christopher") #trouver la position de l'element (.index())
#print(Index)

Compte=liste.count("Max") #compte le nombre d'elements "Max" dans la liste

#liste.sort() #trie les elements par ordre alphabetique
#print(liste)

#Pour une liste trier on utilise la fonction "sorted()" Exemple:

liste_trie = sorted(liste)
#liste_trie.reverse() -> Affiche la liste (liste_trie) a l'inverse
#print(liste) --> cela affiche la liste originale 
#Pour enlever un element de notre liste par son index nous allons utiliser la fonction pop() 
element_enlever = liste_trie.pop(-1)
print(element_enlever)
print(liste_trie)
liste.clear() #enleve tout les elements de la liste
#print (liste)

#joindre les elements d'une liste on utilise join Exemple: " ".join(nom_de_la_liste)
#la methode split() permet de separer les elements en la convertissant vers une liste

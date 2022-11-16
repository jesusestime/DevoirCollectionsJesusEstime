# Ajout d'un title du question numero 1

print("\nQuestion I : Liste\n")




# Création et remplissage du liste de 10 éléments de type chaîne de caractères
Provinces_burundi = ["Province de Bururi","Province de Bubanza", "Province de Bujumbura Mairie", "Province de Bujumbura","Province de Cankuzo", "Province de Cibitoke", "Province de Gitega", "Province de Karuzi", "Province de Kayanza", "Province de Kirundo"]

# Affichage des éléments de la liste
for p in Provinces_burundi :
    print(p)

# Changement du contenu de l'élément numéro 5 de la liste
Provinces_burundi[4]="Province de Ruyigi"

# Ajout d'un élément à la fin de la liste
Provinces_burundi.append("Province de Rumonge")

# Ajout d'un élément à l’index numéro 2 de la liste
Provinces_burundi.insert(2,"Province de Muramvya")

# Suppression de l'élément numéro 3 de la liste
del Provinces_burundi[2]

# Suppression de l'élément à l’index numéro 2 de la liste
Provinces_burundi.pop(2)

#Ordination de la liste
# J'ai préféré ordonner la liste suivant l'ordre alphabétique croissant
Provinces_burundi.sort()

# Suppression de la liste
del Provinces_burundi














# Ajout d'un title du question numero 2
print("\n Question II : Tuple\n")

# Création et remplissage du tuple de 10 éléments de type chaîne de caractères
Provinces_burundi = ("Province de Bujumbura","Province de Bubanza", "Province de Bujumbura Mairie","Province de Bururi", "Province de Cankuzo", "Province de Cibitoke", "Province de Gitega", "Province de Karuzi", "Province de Kayanza", "Province de Kirundo")

# Affichage des éléments du tuple
for p in Provinces_burundi:
    print(p)

# Affichage du contenu de l'élément numéro 5 du tuple
print(Provinces_burundi[4])

#Ordination du tuple
# J'ai préféré ordonner le tuple suivant l'ordre alphabétique croissant
Provinces_burundi_sorted=sorted(Provinces_burundi)










# Ajout d'un title du question numero 3
print("\n Question III : Dictionnaire")


# Création et remplissage du dictionnaire de 10 éléments de type chaîne de caractères ,Il s'agit d'un dictionnaire contenant les provinces du Burundi associés aux clés correspondant à leur abbréviation

Provinces_burundi = {"Bur": "Province de Bururi","Buz":"Province de Bubanza","Bjm": "Province de Bujumbura Mairie","Bj":"Province de Bujumbura","Ckz" : "Province de Cankuzo","Cbt" : "Province de Cibitoke","Gtg": "Province de Gitega","Krz" : "Province de Karuzi","Kyz" :"Province de Kayanza","Krd" :"Province de Kirundo"}



# Affichage des éléments du dictionnaire
for key,value in Provinces_burundi.items():
    print(key +" : "+ value)

# Affichage des clés du dictionnaire
for k in Provinces_burundi.keys():
    print(k)

# Affichage des valeurs du dictionnaire
for k in Provinces_burundi.values():
    print(k)




#Ordination du dictionnaire
# J'ai préféré ordonner mon dictionnaire suivant leur valeurs et par ordre alphabétique croissant
for k in sorted(Provinces_burundi.values()):
    print(k)




# Suppression de l'élément à l’index numéro 2 du dictionnaire 1er phase
# J'ai préféré de trouver  d'abord la clé contenant l'élément à l'index numero 2 pour  me faciliter de l'effacer 
p=[]
for k in Provinces_burundi.keys():
    p.append(k)
print(p[2])

# Suppression de l'élément à l’index numéro 2 du dictionnaire phase final
# Après l'affichage du clé, C'est Bjm pour mon cas du dictionnaire
del Provinces_burundi['Bjm']


# Affichage des nouveaux éléments du dictionnaire
for key,value in Provinces_burundi.items():
    print(key +" : "+ value)


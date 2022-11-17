# Ajout d'un title du question numero 1

print("\nQuestion I : Liste\n")




# Création et remplissage du liste de 10 éléments de type chaîne de caractères
Provinces_burundi = ["Province de Bururi","Province de Bubanza", "Province de Bujumbura Mairie", "Province de Bujumbura","Province de Cankuzo", "Province de Cibitoke", "Province de Gitega", "Province de Karuzi", "Province de Kayanza", "Province de Kirundo"]
print("\n1==========================\n")
# Affichage des éléments de la liste
for p in Provinces_burundi :
    print(p)

print("\n2==========================\n")
# Changement du contenu de l'élément numéro 5 de la liste
numero=5
index=numero-1
Provinces_burundi[index]="Province de Ruyigi"




# Création d'une nouvelle liste en la remplissant avec les éléments de la liste précédente contenant la lettre "a"
print("\n3==========================\n")

# La nouvelle liste crée est Provinces_burundi_contains_letter_a
Provinces_burundi_contains_letter_a=[]

# Ajout les éléments de la liste précédente contenant la lettre "a" dans la nouvelle liste
for p in Provinces_burundi:
    if "a" in p :
        Provinces_burundi_contains_letter_a.append(p)


        

print("\n4==========================\n")
# Ajout d'un élément à la fin de la liste
Provinces_burundi.append("Province de Rumonge")


print("\n5==========================\n")
# Ajout d'un élément à l’index numéro 2 de la liste
index=2
Provinces_burundi.insert(index,"Province de Muramvya")


print("\n6==========================\n")
# Suppression de l'élément numéro 3 de la liste
numero=3
index=numero-1
del Provinces_burundi[index]


print("\n7==========================\n")
# Suppression de l'élément à l’index numéro 2 de la liste
index=2
Provinces_burundi.pop(index)

print("\n8==========================\n")
#Ordination de la liste
# J'ai préféré ordonner la liste suivant l'ordre alphabétique croissant
Provinces_burundi.sort()

print("\n9==========================\n")
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


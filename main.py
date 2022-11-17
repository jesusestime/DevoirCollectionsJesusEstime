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

print("\n10==========================\n")
# Affichage des éléments du tuple en utilisant la boucle while
i=0
while i<len(Provinces_burundi):
    print(Provinces_burundi[i])
    i=i+1

print("\n11==========================\n")
# Affichage du contenu de l'élément numéro 5 du tuple
numero=5
index=numero-1
print(Provinces_burundi[index])

print("\n12==========================\n")
#Ordination du tuple
# J'ai préféré ordonner le tuple suivant l'ordre alphabétique croissant en utilisant la fonction sorted et sortir comme resultat aprés ordination du tuple d'un type tuple qui est Provinces_burundi_sorted 
Provinces_burundi_sorted=tuple(sorted(Provinces_burundi))




















# Ajout d'un title du question numero 3
print("\n Question III : Dictionnaire")


# Création et remplissage du dictionnaire de 10 éléments de type chaîne de caractères ,Il s'agit d'un dictionnaire contenant les provinces du Burundi associés aux clés correspondant à leur abbréviation
Provinces_burundi = {"Bur": "Province de Bururi","Buz":"Province de Bubanza","Bjm": "Province de Bujumbura Mairie","Bj":"Province de Bujumbura","Ckz" : "Province de Cankuzo","Cbt" : "Province de Cibitoke","Gtg": "Province de Gitega","Krz" : "Province de Karuzi","Kyz" :"Province de Kayanza","Krd" :"Province de Kirundo"}


print("\n13==========================\n")
# Affichage des éléments du dictionnaire
for key,value in Provinces_burundi.items():
    print(key +" : "+ value)


print("\n14==========================\n")
# Affichage des clés du dictionnaire
for k in Provinces_burundi.keys():
    print(k)

print("\n15==========================\n")
# Affichage des valeurs du dictionnaire
for v in Provinces_burundi.values():
    print(v)



print("\n16==========================\n")
# Suppression de l'élément à la clé numéro 2 du dictionnaire 1er phase
# J'ai préféré de trouver  d'abord la clé key contenant l'élément à la clé numéro 2 pour  me faciliter de l'effacer
numero=2
index=numero-1
key=""
i=0
for k in Provinces_burundi.keys():
    if i==index :
        key=k
        break
    i=i+1

# Suppression de l'élément à la clé numéro 2 du dictionnaire phase final
# Après la récuperation du clé key on supprime alors cet element donc sa clé et sa valeur dans la dictionnaire
del Provinces_burundi[key]




print("\n17==========================\n")
# Changement de l'élément de la clé numéro 5 du dictionnaire 1er phase
# J'ai préféré de trouver  d'abord la clé key contenant l'élément de la clé numéro 5 pour  me faciliter de l'effacer
numero=5
index=numero-1
key=""
i=0
for k in Provinces_burundi.keys():
    if i==index :
        key=k
        break
    i=i+1

# Changement de l'élément de la clé numéro 5 du dictionnaire phase final
# Après la récuperation du clé key on change alors cet element donc sa valeur correspondant à la clé key dans la dictionnaire
Provinces_burundi[key] = "Province de Muyinga"



print("\n18==========================\n")
# Ajout  d'un nouvel élément dans le dictionnaire Provinces_burundi
Provinces_burundi["Rtn"] = "Province de Rutana"


print("\n19==========================\n")
# Création d'une copie du dictionnaire Provinces_burundi dans un nouveau dictionnaire Provinces_burundi_copy
Provinces_burundi_copy=Provinces_burundi.copy()


print("\n20==========================\n")
# Affichage des nouveaux éléments dans ce nouveau dictionnaire Provinces_burundi_copy
for key,value in Provinces_burundi_copy.items():
    print(key +" : "+ value)



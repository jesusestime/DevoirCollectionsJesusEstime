print("\nQuestion I : Liste\n")

Provinces_burundi = ["Province de Bururi","Province de Bubanza", "Province de Bujumbura Mairie", "Province de Bujumbura","Province de Cankuzo", "Province de Cibitoke", "Province de Gitega", "Province de Karuzi", "Province de Kayanza", "Province de Kirundo"]


for p in Provinces_burundi :
    print(p)


Provinces_burundi[4]="Province de Ruyigi"
    
Provinces_burundi.append("Province de Rumonge")

Provinces_burundi.insert(2,"Province de Muramvya")

del Provinces_burundi[2]

Provinces_burundi.pop(2)

# J'ai préféré ordonner la liste suivant l'ordre alphabétique
Provinces_burundi.sort()

del Provinces_burundi















print("\n Question II : Tuple\n")

Provinces_burundi = ("Province de Bujumbura","Province de Bubanza", "Province de Bujumbura Mairie","Province de Bururi", "Province de Cankuzo", "Province de Cibitoke", "Province de Gitega", "Province de Karuzi", "Province de Kayanza", "Province de Kirundo")


for p in Provinces_burundi:
    print(p)

print(Provinces_burundi[4])

# J'ai préféré ordonner le tuple suivant l'ordre alphabétique
Provinces_burundi_sorted=sorted(Provinces_burundi)


print("\n Question III : Dictionnaire")

Provinces_burundi = {"Bur": "Province de Bururi","Buz":"Province de Bubanza","Bjm": "Province de Bujumbura Mairie","Bj":"Province de Bujumbura","Ckz" : "Province de Cankuzo","Cbt" : "Province de Cibitoke","Gtg": "Province de Gitega","Krz" : "Province de Karuzi","Kyz" :"Province de Kayanza","Krd" :"Province de Kirundo"}


for key,value in Provinces_burundi.items():
    print(key +" : "+ value)

for k in Provinces_burundi.keys():
    print(k)

for k in Provinces_burundi.values():
    print(k)

# J'ai préféré ordonner mon dictionnaire suivant leur valeurs et par ordre alphabétique
for k in sorted(Provinces_burundi.values()):
    print(k)

# J'ai préféré de trouver  d'abord la clé contenant l'élément à l'index numero 2 pour l'effacer 
p=[]
for k in Provinces_burundi.keys():
    p.append(k)
print(p[2])

# C'est Bjm pour mon cas de liste
del Provinces_burundi['Bjm']


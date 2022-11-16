print("\n Question I : Liste")

Provinces_burundi = ["Province de Bubanza", "Province de Bujumbura Mairie", "Province de Bujumbura", "Province de Bururi", "Province de Cankuzo", "Province de Cibitoke", "Province de Gitega", "Province de Karuzi", "Province de Kayanza", "Province de Kirundo"]


for p in Provinces_burundi :
    print(p)


Provinces_burundi[4]="Province de Ruyigi"
    
Provinces_burundi.append("Province de Rumonge")

Provinces_burundi.insert(2,"Province de Muramvya")

del Provinces_burundi[2]

Provinces_burundi.pop(2)

Provinces_burundi.sort()

del Provinces_burundi















print("\n Question II : Tuple")

Provinces_burundi = ("Province de Bujumbura","Province de Bubanza", "Province de Bujumbura Mairie","Province de Bururi", "Province de Cankuzo", "Province de Cibitoke", "Province de Gitega", "Province de Karuzi", "Province de Kayanza", "Province de Kirundo")


for p in Provinces_burundi:
    print(p)

print(Provinces_burundi[4])

Provinces_burundi_sorted=sorted(Provinces_burundi)
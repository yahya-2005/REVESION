n = int(input("Entrez la taille du tableau : "))
tab= []
T1 = []
for i in range(n):
    element= int(input(f"Entrez l'élément {i+1} : "))
    tab.append(element)
ele = int(input("Entrez un nombre : "))
for i in tab:
    if i != ele:
        T1.append(i)
print("Tableau après la suppression est :", T1)
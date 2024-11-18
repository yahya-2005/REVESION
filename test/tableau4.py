n = int(input("Entrez la taille du tableau : "))
tab= []

for i in range(n):
    element= int(input(f"Entrez l'élément {i+1} : "))
    tab.append(element)
s = 0 
for i in range(n): 
    s += tab[i]
m = s/len(tab)
print("la moyenne est :",m)
n = int(input("Entrez la taille du tableau : "))
tab= []

for i in range(n):
    element= int(input(f"Entrez l'élément {i+1} : "))
    tab.append(element)

element_recherche = int(input("Entrez l'élément à rechercher : "))

compteur = 0
for valeur in tab:
    if valeur == element_recherche:
        compteur += 1

print(f"L'élément {element_recherche} apparaît {compteur} fois.")
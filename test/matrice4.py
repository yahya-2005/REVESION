M = int(input("veuillez entrer le nombre du colonne :" ))
N = int(input("veuillez entrer le nombre du ligne :" ))
matrice = [] 
print("entrez le element de la matrice : " )
for i in range(M):
    ligne = []
    for j in range(N):
        element = float(input(f"entrez les element de la matrice [{i+1},{j+1}] :" ))
        ligne.append(element)
    matrice.append(ligne)
print("entrez le element de la matrice2 : " )
matrice2 = []
for i in range(M):
    ligne2 = []
    for j in range(N):
        element2 = float(input(f"entrez les element de la matrice [{i+1},{j+1}] :" ))
        ligne2.append(element2)
    matrice2.append(ligne2)
matrice_addition = []
for i in range(M):
    ligne_addition = []
    for j in range(N): 
        resultat = matrice[i][j] + matrice2[i][j]
        ligne_addition.append(resultat)
    matrice_addition.append(ligne_addition)
print("la premiere matrice est :")
for i in range(M):
    for j in range(N):
        print(matrice[i][j],end=".")
    print()
print("la deuxieme matrice est :")
for i in range(M):
    for j in range(N):
        print(matrice2[i][j],end=".")
    print()
print("la somme des deux matrice est :")
for i in range(M):
    for j in range(N):
        print(matrice_addition[i][j],end=".")
    print()
M = int(input(" veuillez entrer le nombre du colonne :" ))
N = int(input(" veuillez entrer le nombre du ligne :" ))
matrice = []
print("entrez les elements du tableau : " )
for i in range(M):
    ligne = []
    for j in range(N):
        element = int(input(f"veuillez entre element [{i+1},{j+1}] :" ))
        ligne.append(element)
    matrice.append(ligne)
TR = []
for j in range(M):     
    TR_ligne = []
    for i in range(N):
        TR_ligne.append(matrice[i][j])
    TR.append(TR_ligne)
print("\n la matrice est :")
for i in range(M):
    for j in range(N):
        print(matrice[i][j],end=".")
    print()
print("la matrice transposee est : ")
for j in range(M):
    for i in range(N):
        print(TR[j][i],end=".")
    print()
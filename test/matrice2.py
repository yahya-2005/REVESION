M = int(input(" veuillez entrer nombre du colonne : " ))
N = int(input(" veuillez entrer nombre du ligne : " ))
matrice = []
print("entrez les elements de la matrice : " )
for i in range(M): 
    ligne = []
    for j in range(N): 
        element = float(input(f" entrer element de la matrice [{i+1},{j+1}] : " ))
        ligne.append(element)
    matrice.append(ligne)
s = 0 
for i in range(M):
    for j in range(N): 
        s += matrice[i][j]
    print()
print ("la somme des element est :", s )
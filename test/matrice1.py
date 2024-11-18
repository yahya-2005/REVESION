M = int(input("veuillez entrer le nombre du colonne : " ))
N = int(input("veuillez entrer le nombre du ligne: " ))
matrice = []
print("entrez les element de la matrice ")
for i in range(M) :
    ligne=[]
    for j in range(N) : 
        element = int(input(f"veuillez entrer l'element [{i+1},{j+1}] :" ))
        ligne.append(element)
    matrice.append(ligne)
print("\nla matrice est :")
for i in range(M): 
    for j in range(N):
        print(matrice[i][j],end=" . ")
    print()
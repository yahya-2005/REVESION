N = int(input("veuillez entrer la taille de la matrice :" ))
matrice = []
print("entrer les element de la matrice : ")
for i in range(N): 
    ligne = []
    for j in range(N):
        element = int(input(f"veuillez entrer les elements [{i+1},{j+1}] : "))
        ligne.append(element)
    matrice.append(ligne)
symetrique = True 
for i in range(N):
    for j in range(i+1,N):
        if matrice[i][j] != matrice[j][i]:
            symetrique = False 
if symetrique : 
    print("la matrice est symetrique ")
else : 
    print("la matrice est n'est pas symetrique ")
M = int(input("entrez le nombre du colonne : "))
N = int(input("entrez le nombre du ligne : "))
matrice = []
print("veuillez entrer les element du tableau :")
for i in range(M):
    ligne = []
    for j in range(N): 
        element = {f"veuillez entrer les element du tableau [{i+1},{j+1}] : "}
        ligne.append(element)
    matrice.append(ligne)
for ligne in matrice:
    print(ligne)
for i in range(M):
    minC = min(matrice[i])
    maxC = max(matrice[i])
    print(f"Ligne {i+1} : min = {minL}, max = {maxL}")
    
for j in range(N):
    minL = matrice[1][j]
    maxL = matrice[1][j]
    for i in range(M):
        if minL > matrice[i][j] :
            minL = matrice[i][j]
        if maxL < matrice[i][j] :
            minL = matrice[i][j]
print(f"le min de la colonne {i+1} est {minL}")
print(f"le max de la colonne {j+1} est {maxL}")
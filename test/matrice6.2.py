M = int(input("Entrez le nombre de colonnes (M) : "))
N = int(input("Entrez le nombre de lignes (N) : "))

matrice = []
print("Veuillez entrer les éléments du tableau :")
for i in range(N):
    ligne = []
    for j in range(M):
        element = int(input(f"Veuillez entrer l'élément [{i+1},{j+1}] : "))
        ligne.append(element)
    matrice.append(ligne)

print("\nMatrice saisie :")
for ligne in matrice:
    print(ligne)

print("\nMinimum et Maximum pour chaque ligne et colonne :")
for i in range(N):
    minL, maxL = matrice[i][0], matrice[i][0]
    for j in range(M):
        if matrice[i][j] < minL:
            minL = matrice[i][j]
        if matrice[i][j] > maxL:
            maxL = matrice[i][j]
    print(f"Ligne {i+1} : min = {minL}, max = {maxL}")

for j in range(M):
    minC, maxC = matrice[0][j], matrice[0][j]
    for i in range(N):
        if matrice[i][j] < minC:
            minC = matrice[i][j]
        if matrice[i][j] > maxC:
            maxC = matrice[i][j]
    print(f"Colonne {j+1} : min = {minC}, max = {maxC}")


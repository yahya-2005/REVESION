n = int(input("Entrez la taille du tableau : "))
tab= []

for i in range(n):
    i = int(input(f"Entrez l'élément {i+1} : "))
    tab.append(i)
print("les element pairs sont :")
for i in tab : 
    if i  % 2 == 0 :
        print(i)
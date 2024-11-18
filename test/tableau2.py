n = int(input("Entrez la taille du tableau : "))
tab= []
for k in range(n):
    ele = int(input(f"Entrez l'élément {k+1} : "))
    tab.append(ele)
i = 0
j = n - 1
while  i < j :
    z = tab[i]
    tab[i] = tab[j]
    tab[j] = z
    i+=1
    j-=1
print("tableau inversé",tab)
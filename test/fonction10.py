def moyenne(liste):
    if len(liste) == 0 : 
        print("la list est vide ")
        return
    else : 
         somme = sum(liste) 
         moyenne = sum(liste) / len(liste)
    print("la moyenne de list des note est ",moyenne)
#appel 
Tab = []
n = int(input("veuillez entrer la taille du tableau : "))
for i in range(n):
    element = float(input(f"veuillez entrer element [{i+1}] : "))
    Tab.append(element)
moyenne(Tab)

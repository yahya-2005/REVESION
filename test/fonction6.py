def comparaison(a,b):
    if a > b :
        print(f"la valeur du {a} est superieur a la valeur du {b}")
    elif a < b :
        print(f"la valeur du {a} est inferireur a la valeur du {b}")
    else : 
        print(f"la valeur du {a} et {b} sont egaux")
#appel 
x = float(input("Veuillez entrer la valeur du premier nombre : "))
y = float(input("Veuillez entrer la valeur du deuxième nombre : "))
comparaison(x,y)
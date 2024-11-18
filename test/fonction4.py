def air_rectangle(L,l):
    air = L*l
    return air
#appel 
L = float(input("Veuillez entrer la valeur de la longeur du rectangle : "))
l = float(input("Veuillez entrer la valeur la largeur du rectangle : "))
print("air du rectengle est : ",air_rectangle(L,l))
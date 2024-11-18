def air_du_cercle(R):
    air = R*R*3.14
    return air 
def  Perimetre_cercle(R):
    Perimetre = 2 * 3.14 * R
    return Perimetre
#appel 
R = float(input("Veuillez entrer la valeur du rayon du cercle : "))
print(f"air du cercle est : {air_du_cercle(R)}")
print(f"perimetre du cercle est : {Perimetre_cercle(R)}")
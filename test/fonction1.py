def operations(a, b):
    somme = a + b
    différence = a - b
    produit = a * b
    if b != 0:
        quotient = a / b
    else:
        quotient = "undefined (division par zéro)"
    print(f"La somme des deux nombres est : {somme}")
    print(f"Le produit des deux nombres est : {produit}")
    print(f"La différence des deux nombres est : {différence}")
    print(f"Le quotient des deux nombres est : {quotient}")

x = float(input("Veuillez entrer la valeur du premier nombre : "))
y = float(input("Veuillez entrer la valeur du deuxième nombre : "))
operations(x, y)

def factorielle(n):
    if n == 0 or n == 1 :
        return 1 
    else : 
        return n * factorielle(n - 1)
#appel 
n = int(input("veuillez entrer la valeur de le nombre n : "))
print(f"le factorielle de {n} est : {factorielle(n)}")
n = int(input("veuillez entrer un nombre (n):"))
for i in range(1,n+1):
    if n % i == 0 :
        print(f"{i+1} est un deviseur de {n}")
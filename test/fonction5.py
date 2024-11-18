def Celsius_Fahrenheit(c):
    F = c * (9/5) + 32 
    return F 
#appel 
c = float(input("veuillez entrer la temperateur en en Celsius : "))
print("la temperateur en fahrenheit est : ",Celsius_Fahrenheit(c))
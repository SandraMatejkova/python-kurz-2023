#Napiš program, který bude obsahovat jednu proměnnou jmeno. Tato proměnná bude obsahovat libovolné křestní jméno (třeba tvoje). 
#Tvůj program vytvoří e-mailovou adresu na základě této proměnné, s doménou czechitas.cz a tuto e-mailovou adresu vypíše.

#Tedy pokud bude hodnota proměnné jmeno například Jindřiška, pak program vypíše Jindřiška@czechitas.cz.

jmeno = input("Napiste sve jmeno: ")
domena = "@czechitas.cz"
print(f"Vase prirazena emailova adresa je: {jmeno}{domena}")
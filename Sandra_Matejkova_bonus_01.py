#Napiš program, který bude obsahovat proměnnou jmeno_a_prijmeni. 
#Obsah proměnné načti od uživatele pomocí funkce input. 
#Tvůj program postupně vypíše několik způsobů formátování jména:
jmeno_a_prijmeni = input("Zadejte prosim sve jmeno a prijmeni: ")

#všechna písmena velká (vypíše např. JANA MALÁ)
print(jmeno_a_prijmeni.upper()) 

#všechna písmena malá (vypíše např. jana malá)
print(jmeno_a_prijmeni.lower())

#standardní varianta - první písmeno velké, další malá (vypíše např. Jana Malá)
print(jmeno_a_prijmeni.title())

#iniciály (vypíše např. J. M.)
jmeno_a_prijmeni_list = jmeno_a_prijmeni.split(" ")
jmeno = jmeno_a_prijmeni_list[0][0]
prijmeni = jmeno_a_prijmeni_list[1][0]
print(jmeno.upper(),'.', prijmeni.upper(),'.') 
    
#křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, tj. první písmeno velké, 
# další malá (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)
if len(jmeno_a_prijmeni_list[0]) < 5:
        print(jmeno_a_prijmeni.title())
else:
    print(jmeno.upper(),'.',jmeno_a_prijmeni_list[1].capitalize())

#Zaexperimentuj s různými vstupy od uživatele (co třeba JaNA maLá?).
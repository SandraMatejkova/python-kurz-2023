#Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

#Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
#Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
#Tvůj program bude obsahovat dvě funkce:

#První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
#Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
#Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé 
# funkce určí její cenu, kterou vypíše uživateli.

#Tipy:

#Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
#Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420".

def phone_num(num):
    if len(num) == 9 or (len(num) == 13 and num[0:4] == '+420'):
        print("Zadane cislo je spravne")
    else:
        print('Zadali jste spatne cislo!')
        exit()

def sms_price(sms):
    price = (len(sms)/100) * 3
    return price

num_input = input("Dobry den! Zadejte prosim telefonni cislo, kam budete chtit zaslat zpravu: ")

phone_num(num_input)

sms_input = input("Nyni prosim zadejte svou zpravu: ")

final_price = sms_price(sms_input)

print(f'Děkujeme! Na telefonni cislo {num_input} jsme zaslali zpravu v cene {final_price}.') 
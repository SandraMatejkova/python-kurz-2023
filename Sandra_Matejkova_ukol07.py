#ukol-07: Evidence aut
class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, tachometr_stav):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
        self.tachometr_stav = tachometr_stav
        self.pocet_dni_zapujceni = 0

    def pujc_auto(self):
         if self.dostupne == True:
            self.dostupne = False
            print('Potvrzuji zapůjčení vozidla')
            #return self.dostupne
         else:
            print('Vozidlo není k dispozici')
    
    def get_info(self):
        return print( f"{self.registracni_znacka} {self.typ_vozidla}")
    
    def vrat_auto(self, pocet_dni_zapujceni):
        cena_den_1 = 400
        cena_den_2 = 300
        if pocet_dni_zapujceni < 7:
            cena = cena_den_1 * pocet_dni_zapujceni
        else:
            cena = cena_den_2 * pocet_dni_zapujceni
        text = print(f'Vysledna cena je: {cena}')
        return text


autopujcovna={}
autopujcovna['Peugeot'] = Auto('4A2 3020', 'Peugeot 403 Cabrio', 47534, 120000)
autopujcovna['Škoda'] = Auto('1P3 4747', 'Škoda Octavia', 41253, 200000)

auto_input = input('Které auto budete chtít? Máme na výběř Škoda nebo Peugeot: ')

if auto_input in autopujcovna:
    print(autopujcovna[auto_input].get_info())
    autopujcovna[auto_input].pujc_auto()
    pocet_dni_input = int(input('Na jak dlouho si auto půjčíte?: '))
    autopujcovna[auto_input].vrat_auto(pocet_dni_input)

    auto_input = input('Které auto budete chtít? Máme na výběř Škoda nebo Peugeot: ')
    if auto_input in autopujcovna:
        print(autopujcovna[auto_input].get_info())
        autopujcovna[auto_input].pujc_auto()
        pocet_dni_input = int(input('Na jak dlouho si auto půjčíte?: '))
        autopujcovna[auto_input].vrat_auto(pocet_dni_input)
    else:
        print('Bohužel tuto značku nemáme.')
else:
    print('Bohužel tuto značku nemáme.')

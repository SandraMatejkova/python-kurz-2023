#Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník. Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit. 
#Obě informace si ulož. Následně naprogramuj následující varianty:
#
#Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
#Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.
#Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem.

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
kod = input("Dobrý den! Zadejte prosím kód součástky: ")

if kod in sklad:
    mnozstvi = int(input("Nyní prosím zadejte množství: "))
    if mnozstvi < sklad[kod]:
        print(f"Požadovaný počet kusů: {mnozstvi} součástky: {kod} máme skladem. Vaše objednávka bude vyřízena v nejbližší době. Děkujeme!")
        sklad[kod] -= mnozstvi
        #print(sklad[kod])
    else:
        print(f'Bohužel požadovaný počet kusů: {mnozstvi} součástky: {kod} nemáme skladem. Bude Vám doručeno {sklad[kod]} kusů. Děkujeme!')
        sklad.pop(kod)
        #print(sklad)
else:
    print(f'Zadaná součástka {kod} bohužel není skladem!')
#1. Pomocí nástroje regex101 vymysli regulární výraz, který označí platná data a neoznačí neplatná data:

#Reseni ukol 1:
#(\d{1,2})(\.|\/|. )(\d{1,2})(\.|\/|. )([\d]{4})

#2. Zkopíruj si obsah souboru posta.txt do regex101 jako testovací řetězec. Vymysli regulární výraz, který označí všechny "poslední řádky adresy" v textu. P
#oslední řádka adresy zpravidla obsahuje PSČ a název obce, například 190 16 PRAHA 916 nebo 742 45 FULNEK. Celkem by jich mělo být 18.

#Reseni ukol 2:

#^\d{3} \d{2}\s{0,}[a-zA-ZáčďéěíňóřšťůúýžÁČĎÉĚÍŇÓŘŠŤŮÚÝŽ]{1,}\s{0,}?[a-zA-ZáčďéěíňóřšťůúýžÁČĎÉĚÍŇÓŘŠŤŮÚÝŽ]{0,} ?[a-zA-ZáčďéěíňóřšťůúýžÁČĎÉĚÍŇÓŘŠŤŮÚÝŽ]{0,} ?[a-zA-ZáčďéěíňóřšťůúýžÁČĎÉĚÍŇÓŘŠŤŮÚÝŽ]{0,} ?\d{0,}$
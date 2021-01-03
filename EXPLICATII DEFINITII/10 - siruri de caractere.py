# ACCESAREA ELEMENTELOR UNUI SIR DE CARACTERE

# Elementele pot fi accesate si cu numere pozitive dar si cu numere negative
# Stringurile nu sunt imutabile, deci sunt read-only.

# MODIFICAREA ELEMENTELOR UNUI SIR DE CARACTERE
    #   sir = sir[:pozitie_caracter] + "caracter_nou" + sir[pozitie_caracter + 1:] -> modifici caract de pe pozitie
    #   sir = sir[:pozitie_caracter] + sir[pozitie_caracter + 1] -> stergi caracterul de pe "pozitie_caracter"

# OPERATORI PT SIRURI DE CARACTERE:
    #   concatenare: se face cu +. "exemplu" + " " + "de" + " " + "concatenare"
    #   multiplicarea unui sir: se face cu *: "test" * 3 = "testtesttest"
    #   testarea apartenentei: operatorul in: "ast" in "asta" = True

# FUNCTII PREDEFINITE PT SIRURI DE CARACTERE:
    #   len(sir) -> numarul de caractere dintr-un sir
    #   srt(sir) -> transforma valoarea expresiei intr-un sir de caractere
    #   min(sir), max(sir) -> furnizeaza caracterul maxim dintr-un sir 
    #   ord(caracter) -> furnizeaza unicode-ul caracterului respectiv
    #   chr(numar) -> furnizeaza caracterul cu unicode-ul numar

# METODE PT PRELUCRAREA SIRURILOR DE CARACTERE

    #   strip([caractere]) -> furnizeaza sirul obtinut prin eliminarea din sirul curent al celui mai lung 
    #                         prefix si sufix formate din caracterele indicate in parametru
    #                         daca metodei nu i se indica parametru, atunci va lua ca parametru automat spatiul
    #   center(latime, caracter) -> furnizeaza sirul obtinut prin centrarea sirului initial folosind "caracter"
    #   format(numar_variabil_de_parametrii) -> inlocuieste campurile marcate cu {} din sirul curent cu 
    #                                           parametrii corespunzatori. poti sa pui si un index intre {}

    #   lower() -> sirul obtinut din sirul initial prin transformarea tuturor literelor mari in litere mici.
    #   upper() -> sirul obtinui din sirul initial prin transformarea tuturor literelor mici in litere mari.
    #   swapcase() -> sirul obtinut din cel initial prin transformarea literelor mari in litere mici si invers.
    #   title() -> sirul obtinut din cel initial prin transformarea primului caracter de la fiecare cuvant in unul mare
    #              si restul mici
    #   capitalize() -> sirul obtinut din cel initial prin transformarea primului caracter in litera mare si restu mici
    
    #   isascii() -> verifica daca toate caracterele sunt in ascii
    #   isalpha() -> verif daca toate caracterele sirului sunt litere.
    #   isdigit() -> verif daca toate caracterele sirului sunt cifre.
    #   isnumeric() -> verif daca toate caracterele sirului sunt numerice.
    #   isalnum() -> verif daca toate caracterele sunt alfanumerice (litere sau cifre)
    #   isspace() -> verif daca toate literele din sir sunt spatii albe
    #   islower() -> __||__ sunt litere mici
    #   isupper() -> __||__ sunt litere mari
    #   istitle() -> verifica daca prima litera a fiecarui cuvant este litera mare

    #   count(subsir, [start], [stop]) -> furnizeaza numarul aparitiilor disjuncte ale subsirului in sirul curent
    #   find(subsir, [start], [stop]) -> cel mai mic indice la care incepe subsirul in sirul curent
    #   rfind(subsir, [start], [stop]) -> cel mai mare indice la care incepe subsirul in sirul curent
    #   startswith(subsir, [start], [stop]) -> verifica daca sirul curent incepe cu subsir
    #   endswith(subsir, [start], [stop]) -> verifica daca sirul curent se termina cu subsir
    #   replace(subsir, subsir_nou, [max]) -> inlocuieste subsirul cu altul. Max indica de cate ori inlocuiesti

    #   split(separator) -> furnizeaza o lista care contine subsirurile obtinute din sirul crt considerand separatorul
    #   join -> furnizeaza sirul obtinut prin concatenarea subsirurilor date, folosind ca separator sirul crt




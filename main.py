from modele.komponenty_magistrali.karta import Karta
from modele.komponenty_obudowy.magistrala import Magistrala
from modele.komponenty_plyty_montazowej.dysk import Dysk
from modele.komponenty_plyty_montazowej.plyta_glowna import PlytaGlowna
from modele.komponenty_obudowy.plyta_montazowa import PlytaMontazowa
from modele.obudowa import Obudowa


def main():

    # KARTY
    karta_1 = Karta(1, 159)

    # DYSKI
    dysk_1 = Dysk(2, 200)
    dysk_2 = Dysk(3, 260)

    # PLYTY GLOWNE
    plyta_glowna_1 = PlytaGlowna(4, 320)
    plyta_glowna_2 = PlytaGlowna(5, 299)

    # MAGISTRALE
    magistrala_1 = Magistrala(6, 400)
    magistrala_1.dodaj_karte(karta_1)

    # PLYTY MONTAZOWE
    plyta_montazowa_1 = PlytaMontazowa(7, 140)
    plyta_montazowa_1.dodaj_dysk(dysk_1)
    plyta_montazowa_1.dodaj_plyte_glowna(plyta_glowna_1)

    plyta_montazowa_2 = PlytaMontazowa(8, 220)
    plyta_montazowa_2.dodaj_dysk(dysk_2)
    plyta_montazowa_2.dodaj_plyte_glowna(plyta_glowna_2)

    # OBUDOWY
    obudowa_1 = Obudowa(5, 30)
    obudowa_1.dodaj_plyte_montazowa(plyta_montazowa_1)
    obudowa_1.dodaj_plyte_montazowa(plyta_montazowa_2)
    obudowa_1.dodaj_magistrale(magistrala_1)
    # Wypisanie zawartości obudowy
    obudowa_1.do_operation()
    # Wypisanie ceny obudowy
    print('Suma cen elementów obudowy 1 to: ', obudowa_1.suma_cen( ))


    print('Suma cen elementów plyty montazowej 1 to: ', plyta_montazowa_1.suma_cen( ))
    print('Suma cen elementów plyty montazowej 2 to: ', plyta_montazowa_2.suma_cen( ))
    print('Suma cen elementów magistrali 1 to: ', magistrala_1.suma_cen( ))






if __name__ == "__main__":
    main( )

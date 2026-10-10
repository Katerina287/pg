def cislo_text(cislo):
    n = int(cislo)
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět",
                "deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", 
                "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", 
               "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    if n < 20:
        return jednotky[n]
    elif n == 100:
        return "sto"
    elif n % 10 == 0:
        return desitky[n // 10]
    else:
        return desitky[n // 10] + " " + jednotky[n % 10]

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)


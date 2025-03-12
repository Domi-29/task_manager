#Task Manager 

#Seznam úkolů
ukoly = []

def hlavni_menu():
    """Hlavní menu správce úkolů."""
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        volba = input("Vyberte možnost (1-4): ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("\nKonec programu.") 
            break 
        else:
            print("Neplatná volba! Zajdajte číslo mezi 1 a 4.")

def pridat_ukol():
    """Funkce pro přidaní nového úkolu."""
    while True:
        nazev = input("\nZadajte název úkolu: ").strip()
        if not nazev:
            print("Název úkolů nemůže být prázdny!")
            continue #Možnost zadat popis znovu

        popis = input("Zadajte popis úkolů: ").strip()
        if not popis:
            print("Popis úkolů neůže být prázdny!")
            continue

       #Pridanie úkolu do seznamu
        ukoly.append((nazev, popis))
        print(f"Úkol '{nazev}' byl přidán.")
        break #Po úspešnom pridaní, končíme funkciu

def zobrazit_ukoly():
    """Zobrazí všechny úkoly."""
    print("\nSeznam úkolů:")
    if not ukoly:
        print("Žádné úkoly nejsou k dispozici.")
    else:
        for i, (nazev, popis) in enumerate(ukoly, start=1):
            print(f"{i}. {nazev} - {popis}")

def odstranit_ukol():
    """Odstraní úkol podle zadaného čísla."""
    if not ukoly:
        print("Seznam úkolů je prázdný, není co odstranit.")
        return
    
    zobrazit_ukoly() #Zobrazí aktuální úkoly 
    
    while True:
        try:
            index = int(input("Zadajte číslo úkolu, který chcete odstranit: "))
            if 1 <= index <= len(ukoly):
                nazev, _ = ukoly.pop(index - 1)
                print(f"Úkol '{nazev}' byl odstraněn.")
                break #Po úspešnom odstranení ukončí cyklus
            else:
                print("Neplatné číslo úkolu! Zadajte číslo z nabídky.")
        except ValueError:
            print("Chyba! Zadajte platné číslo úkolu.")

#Spustenie programu
if __name__ == "__main__":
    hlavni_menu()


from Listy import teatry, klienci, pracownicy
import folium
import webbrowser

# funkcja read
def read_teatry():
    print("Lista teatrów:")
    for teatr in teatry:
        print(f"{teatr['nazwa']}, adres: {teatr['adres']}")


def read_klienci(teatry):
    if teatry in klienci:
        print(f"Klienci {teatry}:")
        for klient in klienci[teatry]:
            print(f"- {klient}")
    else:
        print("Nie znaleziono teatru o podanej nazwie.")


def read_pracownicy(teatry):
    if teatry in pracownicy:
        print(f"Pracownicy {teatry}:")
        for pracownik in pracownicy[teatry]:
            print(f"- {pracownik}")
    else:
        print("Nie znaleziono teatru o podanej nazwie.")

def read_współrzędne():
    for teatr in teatry:
        print(f"Nazwa: {teatr['nazwa']}, Współrzędne: {teatr['współrzędne']}")

# Funkcja create
def create_teatry(nazwa,adres):
    teatry.append({'nazwa': nazwa, 'adres': adres})
    print(f"Dodano teatr: {nazwa}, adres: {adres}")


def create_klienci(teatr, klient, spektakle):
    if teatr in klienci:
        klienci[teatr][klient] = spektakle
    else:
        klienci[teatr] = {klient: spektakle}
    print(f"Dodano klienta {klient} do teatru {teatr}")


def create_pracownicy(teatr, pracownik):
    if teatr in pracownicy:
        pracownicy[teatr].append(pracownik)
    else:
        pracownicy[teatr] = [pracownik]
    print(f"Dodano pracownika {pracownik} do teatru {teatr}")

def create_wspolrzedne(nazwa, adres, wspolrzedne):
    teatry.append({'nazwa': nazwa, 'adres': adres, 'współrzędne': wspolrzedne})
    print(f"Dodano współrzędne dla teatru {nazwa}")

# Funkcja update
def update_teatry(nazwa, nowy_adres):
    for teatr in teatry:
        if teatr['nazwa'] == nazwa:
            teatr['adres'] = nowy_adres
            print(f"Zaktualizowano adres teatru {nazwa} na {nowy_adres}")
            return
    print("Nie znaleziono teatru o podanej nazwie.")


def update_klienci(teatr, klient, nowe_spektakle):
    if teatr in klienci and klient in klienci[teatr]:
        klienci[teatr][klient] = nowe_spektakle
        print(f"Zaktualizowano spektakle klienta {klient} w teatrze {teatr}")
    else:
        print("Nie znaleziono klienta lub teatru o podanej nazwie.")


def update_pracownicy(teatr, stary_pracownik, nowy_pracownik):
    if teatr in pracownicy and stary_pracownik in pracownicy[teatr]:
        pracownicy[teatr] = [nowy_pracownik if p == stary_pracownik else p for p in pracownicy[teatr]]
        print(f"Zaktualizowano pracownika {stary_pracownik} na {nowy_pracownik} w teatrze {teatr}")
    else:
        print("Nie znaleziono pracownika lub teatru o podanej nazwie.")

def update_współrzędne(nazwa, nowe_współrzędne):
    for teatr in teatry:
        if teatr['nazwa'] == nazwa:
            teatr['współrzędne'] = nowe_współrzędne
            print(f"Zaktualizowano współrzędne teatru {nazwa} na {nowe_współrzędne}")
            return
    print("Nie znaleziono teatru o podanej nazwie.")
# Funkcja remove
def remove_teatry(nazwa):
    global teatry
    for teatr in teatry:
        if teatr['nazwa'] == nazwa:
            teatry.remove(teatr)
            print(f"Usunięto teatr {nazwa}")
            return
    print(f"Nie znaleziono teatru o nazwie {nazwa}")


def remove_klienci(teatr, klient):
    if teatr in klienci and klient in klienci[teatr]:
        klienci[teatr].remove(klient)
        print(f"Usunięto klienta {klient} z teatru {teatr}")
    else:
        print(f"Nie znaleziono klienta {klient} lub teatru {teatr} o podanej nazwie.")


def remove_pracownicy(teatr, pracownik):
    if teatr in pracownicy and pracownik in pracownicy[teatr]:
        pracownicy[teatr].remove(pracownik)
        print(f"Usunięto pracownika {pracownik} z teatru {teatr}")
    else:
        if teatr not in pracownicy:
            print(f"Nie znaleziono teatru o nazwie {teatr}.")
        else:
            print(f"Nie znaleziono pracownika {pracownik} w teatrze {teatr}.")

def remove_współrzędne(nazwa):
    global teatry
    teatry = [teatr for teatr in teatry if teatr['nazwa'] != nazwa]
    print(f"Usunięto współrzędne teatru {nazwa}")


def generuj_mape_teatrow(teatry):
    # Utworzenie mapy centrowanej na środku zakresu współrzędnych teatrów
    m = folium.Map(location=[52.235, 21.015], zoom_start=13)

    # Dodanie markerów dla każdego teatru
    for teatr in teatry:
        nazwa = teatr['nazwa']
        adres = teatr['adres']
        wspolrzedne = teatr['współrzędne']
        lat, lon = map(float, wspolrzedne.split(', '))
        folium.Marker(
            location=[lat, lon],
            popup=f"{nazwa}<br>{adres}",
            tooltip=nazwa
        ).add_to(m)

    # Zapisanie mapy do pliku HTML
    nazwa_pliku = 'mapa_teatrow.html'
    m.save(nazwa_pliku)
    print(f"Mapa została wygenerowana i zapisana jako '{nazwa_pliku}'.")

    # Otwórz plik w przeglądarce
    webbrowser.open(nazwa_pliku)

# Wywołanie funkcji generującej mapę
generuj_mape_teatrow(teatry)

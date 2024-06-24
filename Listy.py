
# zdefiniowanie listy teatrów
teatry: list[dict] = [
    {'nazwa': 'Teatr Wielki', 'adres': 'plac Teatralny 1', 'współrzędne' : '52.2431, 21.0095'},
    {'nazwa': 'Teatr Narodowy', 'adres': 'plac Teatralny 3','współrzędne': '52.2434, 21.0098'},
    {'nazwa': 'Teatr Powszechny im. Zygmunta Hübnera', 'adres': 'ul.Jana Zamoyskiego 20','współrzędne': '52.2474, 21.0347'},
    {'nazwa': 'Teatr Dramatyczny m.st. Warszawy', 'adres': 'plac Defilad 1','współrzędne': '52.2317, 21.0053'},
    {'nazwa': 'Teatr Współczesny w Warszawie', 'adres': 'ul.Mokotowska 13','współrzędne': '52.2365, 21.0287'},
]

# zdefiniowanie listy klientów poszczególnych teatrów wraz z obejrzanymi przez nich spektaklami
klienci = {
    'Teatr Wielki': {
        'Jan Kowalski': ['Ambasador', 'Bal manekinów'],
        'Anna Nowak': ['Czarownice z Salem', 'Dziady cz.I'],
        'Marek Zalewski': ['Emigranci', 'Hedda Gabler'],
    },
    'Teatr Narodowy': {
        'Magda Kowalczyk': ['Kalkwerk', 'Lorenzaccio'],
        'Jacek Wójcik': ['Matka', 'Niespodzianka'],
        'Paweł Zieliński': ['Ożenek', '	Pułapka'],
    },
    'Teatr Powszechny im. Zygmunta Hübnera': {
        'Katarzyna Kwiatkowska': ['	Rewizor', 'Samobójca'],
        'Krzysztof Zając': ['W małym dworku', 'Wujaszek Wania'],
        'Dorota Czarnecka': ['Hamlet', 'Mistrz'],
    },
    'Teatr Dramatyczny m.st. Warszawy': {
        'Michał Piotrowski': ['Otello', 'Proces'],
        'Monika Piotrowska': ['Stalin', 'Zbrodnia i kara'],
        'Zofia Piotrowska': ['Noc listopadowa', 'Ławeczka'],
    },
    'Teatr Współczesny w Warszawie': {
        'Sylwia Kamińska': ['Świętoszek', 'Parady'],
        'Rafał Kamiński': ['Pułapka', 'Ostatnia taśma'],
        'Zbigniew Zając': ['Samobójca', 'Spiskowcy'],
    },
}

# zdefiniowanie listy pracowników listy poszczególnych teatrów
pracownicy = {
    'Teatr Wielki': ['Marcin Kowalski', 'Tomasz Nowak', 'Anna Pawlak', 'Dominik Król'],
    'Teatr Narodowy': ['Tomasz Nowak', 'Andrzej Martyniuk', 'Jacek Pawlak' 'Antonina Kot'],
    'Teatr Powszechny im. Zygmunta Hübnera': ['Jacek Król', 'Dominika Wićkowska', 'Adam Mróz', 'Jan Miód'],
    'Teatr Dramatyczny m. st. Warszawy': ['Paweł Kwiatkowski', 'Karol Kwiatkowski', 'Jagoda Szymczuk', 'Sławomir Gola'],
    'Teatr Współczesny w Warszawie': ['Krzysztof Lewandowski', 'Dominik Nowicki']
}

# funkcja read
def read_teatry():
    print("Lista teatrów:")
    for teatr in teatry:
        print(f"- {teatr['nazwa']}, adres: {teatr['adres']}")

def read_klienci(teatr):
    if teatr in klienci:
        print(f"Klienci {teatr}:")
        for klient in klienci[teatr]:
            print(f"- {klient}")
    else:
        print("Nie znaleziono teatru o podanej nazwie.")

def read_pracownicy(teatr):
    if teatr in pracownicy:
        print(f"Pracownicy {teatr}:")
        for pracownik in pracownicy[teatr]:
            print(f"- {pracownik}")
    else:
        print("Nie znaleziono teatru o podanej nazwie.")

# Funkcja create
def create_teatr(nazwa, adres):
    teatry.append({'nazwa': nazwa, 'adres': adres})
    print(f"Dodano teatr: {nazwa}, adres: {adres}")

def create_klient(teatr, klient, spektakle):
    if teatr in klienci:
        klienci[teatr][klient] = spektakle
    else:
        klienci[teatr] = {klient: spektakle}
    print(f"Dodano klienta {klient} do teatru {teatr}")

def create_pracownik(teatr, pracownik):
    if teatr in pracownicy:
        pracownicy[teatr].append(pracownik)
    else:
        pracownicy[teatr] = [pracownik]
    print(f"Dodano pracownika {pracownik} do teatru {teatr}")

# Funkcja update
def update_teatr(nazwa, nowy_adres):
    for teatr in teatry:
        if teatr['nazwa'] == nazwa:
            teatr['adres'] = nowy_adres
            print(f"Zaktualizowano adres teatru {nazwa} na {nowy_adres}")
            return
    print("Nie znaleziono teatru o podanej nazwie.")

def update_klient(teatr, klient, nowe_spektakle):
    if teatr in klienci and klient in klienci[teatr]:
        klienci[teatr][klient] = nowe_spektakle
        print(f"Zaktualizowano spektakle klienta {klient} w teatrze {teatr}")
    else:
        print("Nie znaleziono klienta lub teatru o podanej nazwie.")

def update_pracownik(teatr, stary_pracownik, nowy_pracownik):
    if teatr in pracownicy and stary_pracownik in pracownicy[teatr]:
        pracownicy[teatr] = [nowy_pracownik if p == stary_pracownik else p for p in pracownicy[teatr]]
        print(f"Zaktualizowano pracownika {stary_pracownik} na {nowy_pracownik} w teatrze {teatr}")
    else:
        print("Nie znaleziono pracownika lub teatru o podanej nazwie.")

# Funkcja remove
def remove_teatr(nazwa):
    global teatry
    teatry = [teatr for teatr in teatry if teatr['nazwa'] != nazwa]
    print(f"Usunięto teatr {nazwa}")

def remove_klient(teatr, klient):
    if teatr in klienci and klient in klienci[teatr]:
        del klienci[teatr][klient]
        print(f"Usunięto klienta {klient} z teatru {teatr}")
    else:
        print("Nie znaleziono klienta lub teatru o podanej nazwie.")

def remove_pracownik(teatr, pracownik):
    if teatr in pracownicy and pracownik in pracownicy[teatr]:
        pracownicy[teatr].remove(pracownik)
        print(f"Usunięto pracownika {pracownik} z teatru {teatr}")
    else:
        print("Nie znaleziono pracownika lub teatru o podanej nazwie.")




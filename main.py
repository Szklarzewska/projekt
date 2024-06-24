from Listy import  teatry, klienci, pracownicy
from crud import read_teatry, read_klienci, read_pracownicy, read_współrzędne, create_teatry, create_klienci, create_pracownicy, create_wspolrzedne, update_teatry, update_klienci, update_pracownicy, update_współrzędne,  remove_teatry, remove_klienci, remove_pracownicy, remove_współrzędne


print('Logowanie')
print('Login: Nazwisko twórcy')
print('Haslo: Grupa wydziałowa')
print('')

Login = "Szklarzewska"
Haslo = "WIG23GW4S0"
login: str = input("Podaj login: ")
haslo: str = input("Podaj haslo: ")
if Login == login and Haslo == haslo:
        print("Sukces")
else:
        print("Blędny login lub haslo")
        login: str = input("Podaj login:")
        haslo: str = input("Podaj haslo:")


# funkcja wyświetlająca listę teatrów
def wyswietl_teatry():
    print("Lista teatrów:")
    for teatr in teatry:
        print(f" {teatr['nazwa']}, adres: {teatr['adres']}")


# funkcja wyświetlająca listę klientów okreslonego teatru
def wyswietl_klientow_teatru():
    nazwa_teatru = input("Wpisz nazwę teatru: ")
    print(f"{nazwa_teatru}")

    if nazwa_teatru in klienci:
        print("Lista klientów okreslonego teatru:")
        for klient in klienci[nazwa_teatru]:
            print(f"{klient}")
    else:
        print("Nie znaleziono teatru o podanej nazwie.")


# funkcja wyświetlająca spektakle obejrzane przez wybranego klienta okreslonego teatru
def wyswietl_spektakle_klienta():
    nazwa_teatru = input("Wpisz nazwę teatru: ")

    if nazwa_teatru in klienci:
        nazwa_klienta = input("Wpisz imię oraz nazwisko klienta: ")
        if nazwa_klienta in klienci[nazwa_teatru]:
            print(f"Spektakle obejrzane przez {nazwa_klienta} w {nazwa_teatru}:")
            for spektakl in klienci[nazwa_teatru][nazwa_klienta]:
                print(f"- {spektakl}")
        else:
            print("Nie znaleziono klienta o podanym nazwisku.")
    else:
        print("Nie znaleziono teatru o podanej nazwie.")


# funkcja wyświetlająca listę pracowników dla wybranego teatru
def wyswietl_pracownikow_teatru():
    nazwa_teatru = input("Wpisz nazwę teatru: ")
    print(f"{nazwa_teatru}")

    if nazwa_teatru in pracownicy:
        print("Lista pracowników tego teatru:")
        for pracownik in pracownicy[nazwa_teatru]:
            print(f"{pracownik}")
    else:
        print("Nie znaleziono teatru o podanej nazwie.")

def wyswietl_współrzędne_teatru():
    nazwa_teatru = input("Wpisz nazwę teatru: ")
    print(f"{nazwa_teatru}")

    for teatr in teatry:
        if teatr['nazwa'] == nazwa_teatru:
            print(f"Współrzędne teatru {nazwa_teatru}: {teatr['współrzędne']}")
            return

    print("Nie znaleziono teatru o podanej nazwie.")

def menu():
    while True:
        print("1. Wyświetl listę teatrów")
        print("2. Wyświetl listę klientów wybranego teatru")
        print("3. Wyświetl spektakle obejrzane przez klienta wybranego teatru")
        print("4. Wyświetl listę pracowników wybranego teatru")
        print("5. Wyświetl współrzędne teatru")
        print("6. Dodaj nowy teatr")
        print("7. Dodaj nowego klienta")
        print("8. Dodaj nowego pracownika")
        print("9. Zaktualizuj dane teatru")
        print("10. Zaktualizuj dane klienta")
        print("11. Zaktualizuj dane pracownika")
        print("12. Usuń teatr")
        print("13. Usuń klienta")
        print("14. Usuń pracownika")
        print("15. Wyświetl współrzędne wszystkich teatrów")
        print("16. Dodaj współrzędne teatru")
        print("17. Zaktualizuj współrzędne teatru")
        print("18. Usuń współrzędne teatru")
        print("19. Wyjście")

        wybor = input("Wybierz opcję : ")

        if wybor == '1':
            wyswietl_teatry()
        elif wybor == '2':
            wyswietl_klientow_teatru()
        elif wybor == '3':
            wyswietl_spektakle_klienta()
        elif wybor == '4':
            wyswietl_pracownikow_teatru()
        elif wybor == '5':
            wyswietl_współrzędne_teatru()
        elif wybor == '6':
            nazwa = input("Podaj nazwę teatru: ")
            adres = input("Podaj adres teatru: ")
            create_teatry(nazwa,adres)
        elif wybor == '7':
            teatr = input("Podaj nazwę teatru: ")
            klient = input("Podaj imie i nazwisko klienta: ")
            spektakle = input("Podaj spektakle (oddzielone przecinkami): ").split(', ')
            create_klienci(teatr, klient, spektakle)
        elif wybor == '8':
            teatr = input("Podaj nazwę teatru: ")
            pracownik = input("Podaj imie i  nazwisko pracownika: ")
            create_pracownicy(teatr, pracownik)
        elif wybor == '9':
            nazwa = input("Podaj nazwę teatru: ")
            nowy_adres = input("Podaj nowy adres teatru: ")
            update_teatry(nazwa, nowy_adres)
        elif wybor == '10':
            teatr = input("Podaj nazwę teatru: ")
            klient = input("Podaj imie i nazwisko klienta: ")
            nowe_spektakle = input("Podaj nowe spektakle (oddzielone przecinkami): ").split(', ')
            update_klienci(teatr, klient, nowe_spektakle)
        elif wybor == '11':
            teatr = input("Podaj nazwę teatru: ")
            stary_pracownik = input("Podaj imie i  nazwisko starego pracownika: ")
            nowy_pracownik = input("Podaj imie i nazwisko nowego pracownika: ")
            update_pracownicy(teatr, stary_pracownik, nowy_pracownik)
        elif wybor == '12':
            nazwa = input("Podaj nazwę teatru: ")
            remove_teatry(nazwa)
        elif wybor == '13':
            teatr = input("Podaj nazwę teatru: ")
            klient = input("Podaj imie i nazwisko klienta: ")
            remove_klienci(teatr, klient)
        elif wybor == '14':
            teatr = input("Podaj nazwę teatru: ")
            pracownik = input("Podaj imie i nazwisko pracownika: ")
            remove_pracownicy(teatr, pracownik)
        elif wybor == '15':
            read_współrzędne()
        elif wybor == '16':
            nazwa = input("Podaj nazwę teatru: ")
            adres = input("Podaj adres teatru: ")
            wspolrzedne = input("Podaj współrzędne teatru: ")
            create_wspolrzedne(nazwa, adres, wspolrzedne)
        elif wybor == '17':
            nazwa = input("Podaj nazwę teatru: ")
            nowe_współrzędne = input("Podaj nowe współrzędne teatru: ")
            update_współrzędne(nazwa, nowe_współrzędne)
        elif wybor == '18':
                nazwa = input("Podaj nazwę teatru, którego współrzędne chcesz usunąć: ")
                remove_współrzędne(nazwa)
        elif wybor == '19':
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

# Wywołanie menu
menu()



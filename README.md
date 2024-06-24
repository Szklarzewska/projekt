nazwa: str = input("Wpisz nazwę teatru: ")
print(f'WITAJ{name}')

# zdefiniowanie listy teatrów
teatry: list = [
    {'nazwa': 'Teatr Wielki - Opera Narodowa', 'adres': 'plac Teatralny 1', 'location'},
    {'nazwa': 'Teatr Narodowy', 'adres': 'plac Teatralny 3', 'location'},
    {'nazwa': 'Teatr Powszechny im. Zygmunta Hübnera', 'adres': ,ul. Jana Zamoyskiego 20', 'location'},
    {'nazwa': 'Teatr Dramatyczny m.st. Warszawy', 'adres': 'plac Defilad 1', 'location'},
    {'nazwa':  'Teatr Współczesny w Warszawie', 'adres': ul. Mokotowska 13', 'location'},
]


# zdefiniowanie listy klientów poszczególnych teatrów wraz z obejrzanymi przez nich spektaklami 
klienci = {
    'Teatr Wielki - Opera Narodowa': {
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
        'Sylwia Kamińska': ['Świętoszek', ''],
        'Rafał Kamiński': ['Spektakl AA', 'Spektakl BB'],
        'Zbigniew Zając': ['Spektakl CC', 'Spektakl DD'],
    },
}
# zdefiniowanie listy pracowników listy poszczególnych teatrów
pracownicy = {
    'Teatr Wielki - Opera Narodowy':['Marcin Kowalski', 'Tomasz Nowak', 'Anna Pawlak', 'Dominik Król'],
    'Teatr Narodowy': ['Tomasz Nowak', 'Andrzej Martyniuk', 'Jacek Pawlak' 'Antonina Kot'],
    'Teatr Powszechny im. Zygmunta Hübnera': ['Jacek Król', 'Dominika Wićkowska', 'Adam Mróz', 'Jan Miód'],
    'Teatr Dramatyczny m. st. Warszawy': ['Paweł Kwiatkowski, 'Karol Kwiatkowski', ,Jagoda Szymczuk', 'Sławomir Gola'],
    'Teatr Współczesny w Warszawie': ['Krzysztof Lewandowski', 'Dominik Nowicki', 'Łukasz Pawlak', 'Anna Król'],
    



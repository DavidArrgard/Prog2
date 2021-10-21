class Fordon:
    def __init__(self, type):
        self.type = type

    def köra(x):
        print(f'Fordornet {x.type} kör iväg')


class Cykel(Fordon):
    def __init__(self, type, antalhjul):
        super().__init__(type)
        self.antalhjul = antalhjul

    def plinga():
        print("pling pling")


class Bil(Fordon):
    def __init__(self, type, modell):
        super().__init__(type)
        self.modell = modell


class Sportbil(Bil):
    def __init__(self, type, modell, hastighet):
        super().__init__(type, modell)
        self.hastighet = hastighet


cykel1 = Cykel("Cykel", 2)
sportbil1 = Sportbil("Sportbil", "Ferrari", 120)

Fordon.köra(sportbil1)
Cykel.plinga()

class Djur:
    def __init__(self, name):
        self.namn = name


class Fagel(Djur):
    def __init__(self, name, vingspann):
        super().__init__(name)
        self.vingspann = vingspann


class Fisk(Djur):
    def __init__(self, name, maxdjup):
        super().__init__(name)
        self.maxdjup = maxdjup


class Torsk(Fisk):
    def __init__(self, name, maxdjup, hastighet):
        super().__init__(name, maxdjup)
        self.hastighet = hastighet


class Haj(Fisk):
    def __init__(self, name, maxdjup, antaltander):
        super().__init__(name, maxdjup)
        self.antaltander = antaltander


haj = Haj("Haj", 20, 30)

torsk = Torsk("Torsk", 30, 35)

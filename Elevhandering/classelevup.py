class Elev:
    def __init__(self, namn, ålder, godkänd):
        self.namn = namn
        self.ålder = ålder
        self.godkänd = godkänd

    def __str__(self):
        if(self.godkänd == "glad"):
            return f"Hen heter {self.namn} och är {self.ålder} gammal och hen är {self.godkänd}"
        else:
            return f"Hen heter {self.namn} och är {self.ålder} gammal och hen är ledsen D:"

    def elev(self):
        return self.namn + self.ålder


elev1 = Elev("David", 18, "glad")
elev2 = Elev("Albin", 18, "integlad")
print(elev1)
print(elev2)

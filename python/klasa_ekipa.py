# class Arbuz:
#     def __init__(self, imie, typ, waga):
#         self.imie = imie
#         self.typ = typ
#         self.waga = waga

#     def przedstaw_sie(self):
#         print(f"Jestem {self.imie}, rzetelnie jestem {self.typ} i ważę {self.waga}kg!")

# # 1. Nasz Pan Arbuz
# pan_arbuz = Arbuz("Pan Arbuz", "Włochem", 8)

# # 2. Jego brat (np. rzetelny siłacz)
# brat_arbuz = Arbuz("Gisberto", "Kulturystą", 15)

# # 3. Kuzyn (np. mały, ale rzetelnie szybki)
# kuzyn_arbuz = Arbuz("Pippo", "Sprinterem", 3)

# # A teraz rzetelnie ich wywołujemy:
# pan_arbuz.przedstaw_sie()
# brat_arbuz.przedstaw_sie()
# kuzyn_arbuz.przedstaw_sie()


class pecora:
    def __init__(self, imie, kolor):
        self.kolor = kolor
        self.imie = imie
    def witaj(self):
        print(f"Jestem {self.imie} ")
        print(f"Moja wełna ma kolor: {self.kolor}")
owieczka = pecora("Owiczka", "Biały")
owieczka2 = pecora("Lucyna", "Czarny")
owieczka3 = pecora("Marysia", "szary")

owieczka.witaj()
owieczka2.witaj()
owieczka3.witaj()
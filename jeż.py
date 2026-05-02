print("SPOTKANIE JEŻA")

class Jez:
    def __init__(self, imie, zapasy, miejsce):
        self.imie = imie
        self.zapasy = zapasy
        self.miejsce = miejsce
    def info(self):
        print(f"jestem Jeż: {self.imie}, mam {self.zapasy} w {self.miejsce}")

riccoli = Jez("Albert", "owada" , "norce")
riccoli2 = Jez("Karol", "ślimaka", "ogrodzie")

riccoli.info()
riccoli2.info()

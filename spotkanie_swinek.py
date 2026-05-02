print("SPOTKANIE ŚWINEK")

class sw_morskie:
    def __init__(self, imie, pokrewienstwo):
        self.imie = imie
        self.pokrewienstwo = pokrewienstwo

    def famiglia(self):
        print(f"Witam jestem {self.imie} i jestem {self.pokrewienstwo} Zygfryda")

swinka1 = sw_morskie("Mariusz", "bratem")
swinka2 = sw_morskie("Sylwia", "siostrą")

swinka1.famiglia()
swinka2.famiglia()

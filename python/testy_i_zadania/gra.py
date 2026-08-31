# Wybór bohatera i wpisanie imienia
# Powitanie gracza

print("Witaj w grze tekstowej\n")
print("Stwórz swoją postać:")

# Imię bohatera
hero_name = input("Podaj imię: ")
print("Witaj,", hero_name)

# Dostępne klasy postaci (oddzielone od wyboru gracza, żeby nie nadpisywać listy)
available_classes = ["Samuraj", "Ronin", "Łuczniczka"]

print("\nDostępne klasy:")
for character in available_classes:
    print(f"- {character}")

chosen_class = input("\nWybierz klasę postaci: ")
print("Wybrałeś:", chosen_class)
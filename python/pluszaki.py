print("--- WIRTUALNA ŁĄCZKA ---")
print("Owieczka stoi na zielonej łączce. W oddali rośnie wielki, stary Dąb.")

# Program pyta użytkownika, co robi Owieczka
decyzja = input("Gdzie idzie Owieczka? (wpisz: deb_usiadz lub laczka_wroc): ")

# Twoja pierwsza zasada: kiedy usiądzie pod Dębem
if decyzja == "deb_usiadz":
    print("\n🌳 Witaj Owieczko!")

# Twoja druga zasada: kiedy wróci z łączki
elif decyzja == "laczka_wroc":
    print("\n👋 Do zobaczenia następnym razem, wpadaj kiedy chcesz!")

# Jeśli wpiszesz coś innego (np. Owieczka pójdzie w las)
else:
    print("\nOwieczka biega beztrosko po polanie...")

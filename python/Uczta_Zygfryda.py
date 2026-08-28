brzuszek = 0
while brzuszek < 100:
    porcja = int(input("Ile gramów karmy sypiesz Zygfrydowi? "))
    brzuszek += porcja
    if brzuszek >= 150:
        print("Zygfryda może boleć brzuszek")
        break
    print(f"W brzuszku jest teraz {brzuszek} gramów karmy")
print("Koniec karmienia. Zygfryd idzie spać. Łiiip!")

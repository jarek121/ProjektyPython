print("KALKULATOR WEŁNY OWIECZEK")
print("")

ships_num = int(input("Ile owieczek jest na pastwisku? "))
wool_num = int(input("Ile kilogramów wełny daje jedna owieczka? "))

whool_sum = ships_num * wool_num

if whool_sum > 50:
    print("Mamy mnóstwo miękkiego runa!")
else:
    print("Trzeba jeszcze trochę poczekać, aż odrośnie")
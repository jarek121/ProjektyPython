pudełko_zdziśka = []
pudełko_zdziśka.append("Kapelusz Arbuza")
pudełko_zdziśka.append("Japko Jeża")
pudełko_zdziśka.append("Bazylia Zygfryda")

print(f"Zdzisiek ma w pudełku: {pudełko_zdziśka}")
pudełko_zdziśka.remove("Bazylia Zygfryda")
for rzecz in pudełko_zdziśka:
    print(f"W pudełku zostało: {rzecz.upper()}")
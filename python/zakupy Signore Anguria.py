zakupy = ["Pomidory", "Ser", "Bazylia"]
# print(f"Pan Arbuz sprawdza listę: {zakupy}")
zakupy.append("oliwa")
zakupy.remove("Pomidory")
# zakupy.reverse()
for produkt in zakupy:
    if produkt == "Bazylia":
        print("Zygfryd! odłóż tę bazylię!")
    else:
        print(f"{produkt} jest bezpieczny w koszyku.")
print(f"Pan Arbuz sprawdza listę: {zakupy}")
# for wypis in zakupy:
#     print(f"Kupić: {wypis}")
# print("LISTA JEST KOMPLETNA")
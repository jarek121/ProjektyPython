for days in range(1, 8):
    if days == 7:
        print(f"Dzień {days}: Pan Jeż zajada marchewkę")
    elif days % 2:
        print(f"Dzień {days}: Pan Jeż zajada jabłuszko")
    else:
        print(f"Dzień {days}: Pan Jeż zajada gruszkę")
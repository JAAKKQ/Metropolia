tuumaa = 0
while tuumaa >= 0:
    tuumaa = int(input("Anna tuumia: "))
    if tuumaa >= 0:
        print(f"{tuumaa} tuuma on {tuumaa*2.54} senttimetriä")

print("Negaatiivinen luku... ohjelma sulkeutuu...")
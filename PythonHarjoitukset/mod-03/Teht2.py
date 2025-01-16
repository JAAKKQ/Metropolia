hytti = input("Mikä on laivan hyttiluokka? (LUX, A, B, C) ")

luokat = {
    "LUX": "LUX on parvekkeellinen hytti yläkannella.",
    "A": "A on ikkunallinen hytti autokannen yläpuolella.",
    "B": "B on ikkunaton hytti autokannen yläpuolella.",
    "C": "C on ikkunaton hytti autokannen alapuolella."
}

try:
    print(f"{luokat[hytti]}")
except:
    print("Virheellinen hyttiluokka")
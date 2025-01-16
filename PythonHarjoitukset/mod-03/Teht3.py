sukupuoli = input("Mikä on sukupuolesi? ")
hemo = int(input("Mikä on hemoglobiiniarvosi (g/l) "))

if sukupuoli.lower() == "mies":
    if hemo >= 134 and hemo <=195:
        print("Hemoglobiiniarvosi on normaali.")
    if hemo > 195:
        print("Hemoglobiiniarvosi on korkea.")
    if hemo < 134:
        print("Hemoglobiiniarvosi on alhainen.")

if sukupuoli.lower() == "nainen":
    if hemo >= 117 and hemo <=175:
        print("Hemoglobiiniarvosi on normaali.")
    if hemo > 175:
        print("Hemoglobiiniarvosi on korkea.")
    if hemo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
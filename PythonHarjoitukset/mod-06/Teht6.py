import math

def pizzaLaskin(halkaisija, hinta):
    sade = halkaisija/2
    pinta_ala = (math.pi*sade**2)*0.0001
    return round(hinta/pinta_ala,2)

pizzat = []


print("Anna ensimmäisen pizzan tiedot:")
halkaisija1 = float(input("Halkaisija (cm): "))
hinta1 = float(input("Hinta (€): "))

print("\nAnna toisen pizzan tiedot:")
halkaisija2 = float(input("Halkaisija (cm): "))
hinta2 = float(input("Hinta (€): "))

yksikkohinta1 = pizzaLaskin(halkaisija1, hinta1)
yksikkohinta2 = pizzaLaskin(halkaisija2, hinta2)

print(f"\nEnsimmäisen pizzan yksikköhinta: {yksikkohinta1:.2f} €/m²")
print(f"Toisen pizzan yksikköhinta: {yksikkohinta2:.2f} €/m²")

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza on paremman vastineen rahalle.")
elif yksikkohinta1 > yksikkohinta2:
    print("Toinen pizza on paremman vastineen rahalle.")
else:
    print("Molemmat pizzat tarjoavat saman vastineen rahalle.")
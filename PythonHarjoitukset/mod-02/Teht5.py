import math

leviska = float(input("Anna leviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

keleven = math.modf(((luoti*13.3)+(13.3*32*naula)+(13.3*32*20*leviska))/1000)

print(f"Massa nykymittojen mukaan:\n{int(keleven[1])} kilogrammaa ja {round(keleven[0]*1000, 2)} grammaa.")
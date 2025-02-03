gallonat = float(input("Anna besiinin määrä Yhdysvaltojen nestegallonoina: "))

def gallonToLiter(gallons):
    return gallons*3.785

print(f"{gallonat} gallonaa on {gallonToLiter(gallonat)} litraa.")
def kausi(kuukausi):
    kaudet = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
    return kaudet[kuukausi-1]

kuukausi_numero = int(input("Anna kuukauden numero: "))

print(f"Antamasi kuukausi numero vastaa {kausi(kuukausi_numero)}kautta")
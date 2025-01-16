import calendar

vuosiluku = int(input("Vuosiluku: "))

if calendar.isleap(vuosiluku):
    print(f"{vuosiluku} on karkausvuosi")
else:
    print(f"{vuosiluku} ei ole karkausvuosi.")
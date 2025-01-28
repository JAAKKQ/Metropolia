luku = input("Anna luku: ")
luvut = []

while luku!="":
    luvut.append(int(luku))
    luku = input("Anna luku: ")
luvut.sort()

print(luvut[-1])
print(luvut[-2])
print(luvut[-3])
print(luvut[-4])
print(luvut[-5])
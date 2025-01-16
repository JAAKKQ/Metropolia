import random

def koodi3():
    return str(random.randint(0,9))
def koodi4():
    return str(random.randint(1,6))


print(f"Kolminumeroinen koodi: {koodi3()+koodi3()+koodi3()}")
print(f"Nelinumeroinen koodi: {koodi4()+koodi4()+koodi4()+koodi4()}")
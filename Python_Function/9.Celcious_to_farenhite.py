# Write a program to convert celcious to farenhite

celcious = float(input("Please enter number in celciuos to convert it into farenhite: "))

def toFarenhite(celcious):
    farenhite = (celcious * 9/5) + 32
    return farenhite

print(f"{toFarenhite(celcious)} F")

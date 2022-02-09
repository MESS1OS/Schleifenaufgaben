# Übungsaufgaben zu Schleifen
# Aufgabe 4
# @Nico Jäger


ANUAL_ROI = 7
YEAR = 365

capital = [1,2,3,4]

startCapital = int(input("Bitte geben sie ihr Start-Kapital ein: "))
targetCapital = int(input("Bitte geben sie ihr gewünschtes End-Kapital ein: "))

capital.append(startCapital)
latestCapital = capital[-1:]

if any(x > targetCapital for x in capital):
    print("test")



while latestCapital < targetCapital:
    tempCapital = capital * (1 + ANUAL_ROI / 100)
    capital.append(tempCapital)
    print(tempCapital, "  ", capital)


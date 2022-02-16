# @Nico Jäger
# Übungsaufgaben zu Schleifen
# Aufgabe 4

import locale

locale.setlocale(locale.LC_ALL, '')

ANUAL_ROI = 10
capital = []
counter = 0

startCapital = int(input("Bitte geben sie ihr Start-Kapital ein: "))
targetCapital = int(input("Bitte geben sie ihr gewünschtes End-Kapital ein: "))

capital.append(startCapital)

for i in range(1, 366, 1):
    latestCapital = capital[-1]
    tempCapital = (latestCapital * (1 + ANUAL_ROI / 100)).__round__(2)
    counter += 1
    capital.append(tempCapital)
    if tempCapital >= targetCapital:
        print("Sie brauchen", counter, "Jahre um ein Kapital von:", locale.currency(latestCapital, grouping=True), "aufzusparen")
        break

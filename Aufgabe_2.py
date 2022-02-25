# @Nico Jäger
# Übungsaufgaben zu Schleifen
# Aufgabe 2

for temperatureF in range(0, 301, 5):
    temperatureC = (temperatureF - 32) * (5/9)
    print(temperatureF, "  ", temperatureC.__round__(4))

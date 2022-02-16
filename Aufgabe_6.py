# @Nico Jäger
# Übungsaufgaben zu Schleifen
# Aufgabe 6


for i in range (0, 3000, 1):
    if (i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0):
        print(i, "ist ein Schaltjahr!")
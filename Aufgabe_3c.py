# Übungsaufgaben zu Schleifen
# Aufgabe 3c
# @Nico Jäger
# y = m*x + b

import numpy as np

m = float(input("Bitte geben sie die Steigung der Funktion an: "))
b = float(input("Bitte geben sie den y-Achsenabschnitt der Funktion an: "))


# Von -5,3 bis +3,5
for x in np.arange(-5.3, 3.6, 0.1):
    y = m * x + b
    print(y)


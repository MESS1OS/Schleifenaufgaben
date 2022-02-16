# @Nico Jäger
# Übungsaufgaben zu Schleifen
# Aufgabe 3d

import numpy as np

# y = m*x + b
# Von -5,3 bis +3,5

count = 0
m = float(input("Bitte geben sie ihren gewünschte Steigung ein: "))
b = float(input("Bitte geben sie den gewünschten Y-Achsen Abstand ein: "))
print("Alle Positiven Werte: ")
for x in np.arange(-5.3, 3.6, 0.1):
    y = m * x + b
    if y > 0:
        count += 1
        print("f(" + str(x.__round__(1)) + ") =", y.__round__(2))
print("Es gibt", count, "positive Funktionswerte")

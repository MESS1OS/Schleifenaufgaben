# @Nico Jäger
# Übungsaufgaben zu Schleifen
# Aufgabe 3b

import numpy as np

# y = m*x + b
# Von -5,3 bis +3,5

m = float(input("Bitte geben sie ihren gewünschte Steigung ein: "))
b = float(input("Bitte geben sie den gewünschten Y-Achsen Abstand ein: "))
for x in np.arange(-5.3, 3.6, 0.1):
    y = m * x + b
    print("f(" + str(x.__round__(1)) + ") =", y.__round__(2))
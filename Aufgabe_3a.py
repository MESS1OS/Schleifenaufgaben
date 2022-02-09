# Übungsaufgaben zu Schleifen
# Aufgabe 3a
# @Nico Jäger

import numpy as np

# y = m*x + b
# Von -5,3 bis +3,5
for x in np.arange(-5.3, 3.6, 0.1):
    print("y = m *", x.__round__(1), "+ b")
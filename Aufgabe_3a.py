# Übungsaufgaben zu Schleifen
# Aufgabe 3a
# @Nico Jäger

import numpy as np

# y = m*x + b
# Y = Dependent variable
# M = Coefficent, Rate and Slope of line
# X = Independent Variable
# B = Y Intercept

# Von -5,3 bis +3,5

m = 10
b = 5
for x in np.arange(-5.3, 3.6, 0.1):
    y = m * x + b
    print("f(" + str(x.__round__(1)) + ") =", y.__round__(2))
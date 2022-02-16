# @Nico Jäger
# Übungsaufgaben zu Schleifen
# Aufgabe 5


inpInteger = input("Bitte geben sie ihre Ganzzahligen Positiven Zahlen ein (Seperator = lehrzeichen): ")
integer = list(map(int, inpInteger.split()))
integer.append(0)
integer.pop()

mean = sum(integer) / len(integer)
print("Ihr Durchschnitt ist:", mean)

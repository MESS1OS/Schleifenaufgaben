# @Nico Jäger
# Übungsaufgaben zu Schleifen
# Aufgabe 1b

import locale

locale.setlocale(locale.LC_ALL, '')

balance = 0

month = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November",
         "Dezember"]

rent = float(input("Wieviel Geld kostet sie Miete im Monat?: "))
electricity = float(input("Wieviel Geld kostet sie Strom im Monat?: "))
water = float(input("Wieviel Geld kostet sie Wasser im Monat?: "))
insurance = float(input("Wieviel Geld kostet sie Versicherung im Monat?: "))
investment = float(input("Wieviel Geld kostet sie Investments im Monat?: "))
wage = float(input("Wieviel Geld verdienen sie im Monat?: "))

fixedExpenses = rent + electricity + water + insurance + investment
fixedIncome = wage
variableIncome = 0
variableExpenses = 0

for i in range(1, 13):
    if i == 12:
        variableExpenses = float(input("Tragen sie hier ihre Außerplanmäßigen Ausgaben ein:  "))
        variableIncome = float(input("Tragen sie hier ihre Außerplanmäßigen Einnahmen ein:  "))

    balance = balance + fixedIncome + variableIncome - fixedExpenses - variableExpenses
    print(str(month[i - 1]) + ":", locale.currency(balance, grouping=True, ))

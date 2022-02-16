# @Nico Jäger
# Übungsaufgaben zu Schleifen

# Aufgabe 1
"""
import locale

locale.setlocale(locale.LC_ALL, '')

balance = 0

rent = 700
electricity = 40
water = 20
insurance = 50
investment = 400

wage = 2700

month = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
cachedBalance = []

FixedExpenses = rent + electricity + water + insurance + investment
FixedIncome = wage


for i in range(1, 12):
    balance = FixedIncome - FixedExpenses
    cachedBalance.append(balance)
    print(str(month[i - 1]) + ":", locale.currency(sum(cachedBalance), grouping=True, ))
"""

# Aufgabe 1a
"""
import locale

locale.setlocale(locale.LC_ALL, '')

balance = 0

month = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
cachedBalance = []

rent = int(input("Wieviel Geld kostet sie Miete im Monat?: "))
electricity = int(input("Wieviel Geld kostet sie Strom im Monat?: "))
water = int(input("Wieviel Geld kostet sie Wasser im Monat?: "))
insurance = int(input("Wieviel Geld kostet sie Versicherung im Monat?: "))
investment = int(input("Wieviel Geld kostet sie Investments im Monat?: "))
wage = int(input("Wieviel Geld verdienen sie im Monat?: "))

FixedExpenses = rent + electricity + water + insurance + investment
FixedIncome = wage


for i in range(1, 12):
    balance = FixedIncome - FixedExpenses
    cachedBalance.append(balance)
    print(str(month[i - 1]) + ":", locale.currency(sum(cachedBalance), grouping=True, ))

"""

# Aufgabe 1b

import locale

locale.setlocale(locale.LC_ALL, '')

balance = 0

month = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November",
         "Dezember"]
cachedBalance = []

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

    balance = fixedIncome + variableIncome - fixedExpenses - variableExpenses
    cachedBalance.append(balance)
    print(str(month[i - 1]) + ":", locale.currency(sum(cachedBalance), grouping=True, ))


# @Nico Jäger
# Übungsaufgaben zu Schleifen
# Aufgabe 1a

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

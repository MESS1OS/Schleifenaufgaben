# Übungsaufgaben zu Schleifen
# Aufgabe 1
# @Nico Jäger

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

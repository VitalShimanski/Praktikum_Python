#!/usr/bin/env python3
def arithmetic(a,b,op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
         return 'Неизвестная операция'

res = arithmetic(489.16,687.3,'/')
print(res)

def is_year_leap(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
def date(day, month, year):
    day_in_month = {1:31,
                    2:29 if is_year_leap(year) else 28,
                    3:31,
                    4:30,
                    5:31,
                    6:30,
                    7:31,
                    8:31,
                    9:30,
                    10:31,
                    11:30,
                    12:31}
    if 1<= month <=12 and 1<= day <= day_in_month[month]:
        return True
    else:
        return False
def date_cheat(day, month, year):
    import datetime
    try:
        datetime.date(year, month, day)
    except ValueError:
        return False
    else:
        return True


res2 = is_year_leap(2028)
print(res2)
res7 = date(20,11,1872)
print(res7)

def date_cheat(day, month, year):
    import datetime
    try:
        datetime.date(year, month, day)
    except ValueError:
        return False
    else:
        return True
res8 = date(16, 4, 2023)
print(res8)
import math
def square(side):
    p = 4 * side
    s = side ** 2
    diag = side * math.sqrt(2)
    return p, s, diag
res3 = square(48)
print(res3)

def season(month):
    if month <= 2 or month == 12:
        return 'Winter'
    elif month <= 5 and month > 2:
        return 'Spring'
    elif month <= 8 and month > 5:
        return 'Summer'
    else:
        return 'Autumn'
res4 = season(9)
print(res4)

def bank(a, years):
    for year in range(years):
        a *= 1.1
    return a
res5 = bank(50000, 12)
print(res5)

def is_prime(x):
    if x == 1:
        return False
    for possible_divisor in range(2,x):
        if x % possible_divisor == 0:
            return False
    else:
        return True
res6 = is_prime(24)
print(res6)

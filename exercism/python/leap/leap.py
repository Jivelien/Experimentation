def is_leap_year(year):
    return any([all([year%4 == 0, year%100 != 0]), year%400 == 0])

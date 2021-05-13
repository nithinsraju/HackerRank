def is_leap(year):
    leap = False
    var = year % 100

    if year % 100 == 0 and year % 400 == 0:
        leap = True
    else:
        leap = False

    if(not leap):
        if year % 4 == 0 and var != 0:
            leap = True

    return leap


year = int(input())
print(is_leap(year))

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    """
        ##########Pseudocode###########
        -> list leap_julian_year
        -> list leap_gregorian_year
        -> list none_leap_julian_year
        -> list none_leap_gregorian_year
        -> list year_1918

        -> if year is leap and its julian:
            -> addition = 0
            -> for month in leap_julian_year:
                -> if addition >= 256:
                    -> day = addition - 256
                    -> month = leap_year.index(month)
                -> addition += month

        -> if year is none_leap and its julian:
            -> addition = 0
            -> for month in none_leap_julian_year:
                -> if addition >= 256:
                    -> day = addition - 256
                    -> month = leap_year.index(month)
                -> addition += month

        -> if year is leap and its Gregorian:
            -> addition = 0
            -> for month in leap_gregorian_year:
                -> if addition >= 256:
                    -> day = addition - 256
                    -> month = leap_year.index(month)
                -> addition += month

        -> if year is none_leap and its Gregorian:
            -> addition = 0
            -> for month in none_leap_gregorian_year:
                -> if addition >= 256:
                    -> day = addition - 256
                    -> month = leap_year.index(month)
                -> addition += month
            
        -> if year is 1918:
            -> addition = 0
            -> for month in year_1918:
                -> if addition >= 256:
                    -> day = addition - 256
                    -> month = leap_year.index(month)
                -> addition += month
            
    return f"{day}.{month}.{year}"
            
    """

    """
        -> list leap_year
        -> list none_leap_year
        -> list year_1918
    """

    leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    none_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year_1918 = [31, 14, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #if year is 1918
    if year == 1918:
        addition = 0
        for i in range(12):
            checks = addition + year_1918[i]
            if checks >= 256:
                day = 256 - addition
                month = f"{i+1:02d}"
                break
            addition = checks

        return f"{day-1}.{month}.{year}"

    leap = False

    #check if year is julian
    if year < 1918:
        #check if year is leap
        if year%4 == 0:
            leap = True

    #check if year is gregorian
    if year > 1918:
        #check if year is leap
        if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
            leap = True

    #leap year
    if leap == True:
        addition = 0
        for i in range(12):
            checks = addition + leap_year[i]
            if checks >= 256:
                day = 256 - addition
                month = f"{i+1:02d}"
                break
            addition = checks
        return f"{day}.{month}.{year}"

    #none_leap year
    if leap == False:
        addition = 0
        for i in range(12):
            checks = addition + none_leap_year[i]
            if checks >= 256:
                day = 256 - addition
                month = f"{i+1:02d}"
                break
            addition = checks
        return f"{day}.{month}.{year}"


print(dayOfProgrammer(1918))
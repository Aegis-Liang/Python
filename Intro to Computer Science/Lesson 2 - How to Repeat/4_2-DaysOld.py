# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    days = 0
    while(year1 <= year2):
        while(month1 <= 12):
            if(year1 == year2) and (month1 == month2):
                return days + day2 - day1
            if(month1 == 12):
                days = days + 31
                year1 = year1 + 1
                month1 = 1
                break
            else:
                if month1 == 2:
                    if year1 % 400 == 0:
                        days = days + 29
                    elif year1 % 100 == 0:
                        days = days + 28
                    elif year1 % 4 == 0:
                        days = days + 29
                    else:
                        days = days + 28
                else:
                    days = days + daysOfMonths[month1-1]
                month1 = month1 + 1


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        print result
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

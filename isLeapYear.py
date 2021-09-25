def isleapyear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif 0 == year % 4:
        return True


year = int(input("Enter the year : "))

if isleapyear(year):
    print("The is leap year ")

else:
    print("Its not a leap year")

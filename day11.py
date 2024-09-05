print("Calculate number of seconds in a year")
print()
oneminute = 60
onehour = 60 * oneminute
oneday = 24 * onehour
oneyear = 365 * oneday
leapyear = 366 * oneday
leap_year = input("Is it a leap year? ")
if leap_year == "yes":
  print("There are", leapyear, "seconds in a leap year")
else:
  print("There are", oneyear, "seconds in a year")
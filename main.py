print("Minutes In Year Calculator")

days_this_year = int(input("How many days are in this year? "))

seconds_in_minute = 60
minutes_in_hour = 60
hours_in_day = 24
days_in_year = 365
days_in_leap_year = 366

if days_this_year == 366:
  seconds_in_leap_year = seconds_in_minute * minutes_in_hour * hours_in_day * days_in_leap_year
  print(f"There are {seconds_in_leap_year} seconds in a leap year")
elif days_this_year == 365:
  seconds_in_year = seconds_in_minute * minutes_in_hour * hours_in_day * days_in_year
  print(f"There are {seconds_in_year} seconds in a year")
else:
  print("Please enter a valid number of days.")

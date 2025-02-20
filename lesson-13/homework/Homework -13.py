# Homework-13

#1. Age Calculator: Ask the user to enter their birthdate.
# Calculate and print their age in years, months, and days.

from datetime import datetime

age = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.strptime(age, "%Y-%m-%d").date()
today = datetime.today().date()

years = today.year - dob.year
months = today.month - dob.month
days = today.day - dob.day

print(f"Your age is {years} years,{months} months,{days} days. ")


#2. Days Until Next Birthday: Similar to the first exercise, but this time,
#  calculate and print the number of days remaining until the user's next birthday.

from datetime import date

dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.strptime(dob_str, "%Y-%m-%d").date()

today = date.today()

next_birthday = date(today.year, dob.month, dob.day)

if next_birthday < today:
    next_birthday = date(today.year + 1, dob.month, dob.day)

days_remaining = (next_birthday - today).days
print(f"Your next birthday is in {days_remaining} days!")


#3. Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes.
#  Calculate and print the date and time when the meeting will end.

from datetime import timedelta

current_date_str = input("Enter the current date (YYYY-MM-DD HH:MM):")
current_date = datetime.strptime(current_date_str,"%Y-%m-%d %H:%M")

h = int(input("Enter the meeting duration(in hours): "))
m = int(input("Enter the meeting duration(in minutes): "))

duration = timedelta(hours=h, minutes=m)

end_time = current_date + duration
print(f"The meeting will end on {end_time}")

#4.Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone,
# and then convert and print the date and time in another timezone of their choice.

import pytz

print("Example Timezones: America/New_York, Europe/London, Asia/Kolkata, UTC, Australia/Sydney")

date_str = input("Enter your date and time (YYYY-MM-DD HH:MM): ")
current_tz_str = input("Enter your timezone: ")
target_tz_str = input("Enter the timezone to convert to: ")


try:
    simple_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    current_tz = pytz.timezone(current_tz_str)
    target_tz = pytz.timezone(target_tz_str)

    date_with_utc = current_tz.localize(simple_date)

    target_date = date_with_utc.astimezone(target_tz)

    print(f"\nOriginal Date & Time in {current_tz_str}: {date_with_utc.strftime('%Y-%m-%d %H:%M %Z%z')}")
    print(f"Converted Date & Time in {target_tz_str}: {target_date.strftime('%Y-%m-%d %H:%M %Z%z')}\n")


except pytz.UnknownTimeZoneError:
    print("Invalid timezone! Please enter a correct timezone name.")
except ValueError:
    print("Invalid date/time format! Please enter in YYYY-MM-DD HH:MM format.")

#5. Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time
# and then continuously print the time remaining until that point in regular intervals (e.g., every second).


from datetime import datetime
import time

future_date_str = input("Enter the future date and time (YYYY-MM-DD HH:MM:SS): ")
future_datetime = datetime.strptime(future_date_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    remaining_time = future_datetime - now

    if remaining_time.total_seconds() <= 0:
        print("\nTime's up!")
        break

    days = remaining_time.days
    seconds = remaining_time.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    print(f"\r⏳ Time remaining: {days} days, {hours:02}:{minutes:02}:{seconds:02}", end="")
    time.sleep(1)

    



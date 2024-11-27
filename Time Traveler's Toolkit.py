# create initial version of Time Traveler's Toolkit

import custom_module as cm
import datetime as dt
import decimal as decimal
from random import randint
from random import choice

# Captue current date and time
date = dt.datetime.today()
time = dt.datetime.now().time()

print(f"Today's date is {date}. The current {time}.")

# Calculate cost of time travel
base_cost = decimal.Decimal("2000.00")
target_year = input("Enter the target year for time travel: ")

true_cost = abs()
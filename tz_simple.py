import pytz
from datetime import datetime

naive_date1 = datetime(2023, 1, 30, 10, 30)
naive_date2 = datetime(2023, 1, 30, 10, 45)
print(f"date1: {naive_date1}")
print(f"date2: {naive_date2}")

diff = naive_date2 - naive_date1
print(f"naive diff: {diff}\n")

tz_pt = pytz.timezone('America/Los_Angeles')
tz_et = pytz.timezone('America/New_York')
# tz_bt = pytz.timezone('Europe/London')

aware_date1 = tz_pt.localize(naive_date1)
aware_date2 = tz_et.localize(naive_date2)

print(f"aware_date1: {aware_date1}")
print(f"aware_date2: {aware_date2}")

diff = aware_date1 - aware_date2
print(f"aware diff: {diff}")

print(pytz.common_timezones)

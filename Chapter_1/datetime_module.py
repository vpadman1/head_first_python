import datetime
print(datetime.date.today())
print("\n")
print(datetime.date.today().day)
print("\n")
print(datetime.date.today().month)
print("\n")
print(datetime.date.today().year)
print("\n")
print(f"Today's date in is format: {datetime.date.isoformat(datetime.date.today())}")

import time
print(time.strftime("%H:%M"))
print("\n")
print(time.strftime("%A %p"))
print("\n")
print(f'Date: {datetime.date.today()} Time: {time.strftime("%H:%M")},Work Week: {time.strftime("%A %p")}')

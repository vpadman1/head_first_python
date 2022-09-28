import time
day = time.strftime("%A")
if day == "Sunday":
    print("party")
elif day == "Wednesday":
    print("Work")
else:
    print("relax")
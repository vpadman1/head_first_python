import time
import random
from datetime import datetime

odds  = [1,3,5,7,9,11,13,15,17,19,21,
        23,25,27,29,31,33,35,37,39,41,
        43,45,47,49,51,53,55,57,59]

for _ in range(5):
    right_this_min = datetime.today().minute
    if right_this_min in odds:
        print("this number is a little odd")
    else:
        print("its even")
    wait_time = random.randint(1,60)
    time.sleep(wait_time)
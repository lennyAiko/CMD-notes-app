### RETURNS THE TIME AND DATE

from datetime import datetime

def get_time_date():
    now_date = datetime.now().strftime("%Y-%m-%d")

    now_time = datetime.now().time().strftime("%H:%M:%S")

    return now_date, now_time

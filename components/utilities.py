import json
import os
from datetime import date, timedelta

def get_settings():
    f = open("settings/settings.json")
    settings = json.load(f)
    f.close()
    return settings

def get_page_settings(name):
    settings = get_settings()
    return settings["pages"][name]

def get_module_name(name):
    return os.path.basename(name).replace(".py", "")

def get_start_date():
    dt = date.today()
    day_of_week = dt.weekday()
    # If it's Sat or Sun back off to prior Fri
    if day_of_week == 6:
        dt = dt - timedelta(2)
    elif day_of_week == 5:
        dt = dt - timedelta(1)
    #format date to 20221405
    return str(dt.year) + str(dt.month).zfill(2) + str(dt.day).zfill(2)



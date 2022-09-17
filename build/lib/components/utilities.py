import json
import os

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


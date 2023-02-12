# MIT License
# Copyright (c) 2023 BIKASH 
import re
from os import environ

search = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
API_ID = environ.get("API_ID", "")
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Bot setting
PICS = (environ.get('PICS', 'https://telegra.ph/file/8b42f6caf6ef5fd76766f.jpg https://telegra.ph/file/82b5bbbab6d5e5593b6b2.jpg'))

# Admins, Channels & Users
ADMINS = environ.get("ADMINS", "")
SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "TechProjectsChats")
AUTH_CHANNEL = environ.get("AUTH_CHANNEL", "")
CHANNELS = [int(ch) if search.search(ch) else ch for ch in os.environ.get("CHANNELS", "0").split()]
LOG_CHANNEL = environ.get("LOG_CHANNEL", "0")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "tgmoviebot")

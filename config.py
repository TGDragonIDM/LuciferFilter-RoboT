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
API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Bot setting
PICS = (environ.get("PICS", ""))

# Admins, Channels & Users
ADMINS = environ.get("ADMINS", "")
SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "TechProjectsChats")
AUTH_CHANNEL = environ.get("AUTH_CHANNEL", "")
CHANNELS = [int(ch) if search.search(ch) else ch for ch in environ.get("CHANNELS", "0").split()]
LOG_CHANNEL = environ.get("LOG_CHANNEL", "")
DELETE_CHANNELS = [int(dch) if search.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
AUTH_GROUPS = environ.get("AUTH_GROUPS", "")
AUTH_USERS = environ.get("AUTH_USERS", "")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "")

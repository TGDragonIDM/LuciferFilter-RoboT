# MIT License
# Copyright (c) 2023 BIKASH 
from os import environ
from config import ( is_enabled, search, API_ID, API_HASH, BOT_TOKEN, PICS, ADMINS, CHANNELS, AUTH_USERS, AUTH_CHANNEL, AUTH_GROUPS, DATABASE_URI, DATABASE_NAME, LOG_CHANNEL, SUPPORT_CHAT, DELETE_CHANNELS )
from LuciferFilter_Robot.translation import Script 

# Bot information
API_ID = API_ID
API_HASH = API_HASH
BOT_TOKEN = BOT_TOKEN

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = PICS.split()

# Admins, Channels & Users
ADMINS = [int(admin) if search.search(admin) else admin for admin in ADMINS.split()]
CHANNELS = CHANNELS
AUTH_USERS = (AUTH_USERS + ADMINS) if AUTH_USERS else []
AUTH_CHANNEL = int(AUTH_CHANNEL) if AUTH_CHANNEL and search.search(AUTH_CHANNEL) else None
AUTH_GROUPS = [int(ch) for ch in AUTH_GROUPS.split()] if AUTH_GROUPS else None

# MongoDB information
DATABASE_URI = DATABASE_URI
DATABASE_NAME = DATABASE_NAME
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
PORT = environ.get("PORT", "8080")
LOG_CHANNEL = int(LOG_CHANNEL)
SUPPORT_CHAT = SUPPORT_CHAT
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{Script.CUSTOM_FILE_CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>🎬 Title:</b> <a href={url}>{title}</a> [{year}] —<b>{kind}</b>\n\n<b>📆 Release:</b> <a href={url}/releaseinfo>{release_date}</a>\n<b>🌟 Rating:</b> <a href={url}/ratings>{rating} / 10</a>\n(based on <code>{votes}</code> user ratings.)\n\n<b>🎭 Genres:</b> #{genres}\n<b>📀 Runtime:</b> <code>{runtime} minutes</code>\n\n<b>☀️ Languages:</b> #{languages}\n<b>🌎 Country of Origin:</b> #{countries}\n<b>🎥 Director:</b> {director}\n\n<b>✍️ Note:</b> <s>This message will be Auto-deleted after 10 hours to avoid copyright issues.</s>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

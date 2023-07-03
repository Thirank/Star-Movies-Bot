import re
from os import environ
from time import time
from os import getenv

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '11973721'))
API_HASH = environ.get('API_HASH', '5264bf4663e9159565603522f58d3c18')
BOT_TOKEN = environ.get('BOT_TOKEN', "5777457260:AAEfAMULHIjj7P__22qSvoT9ygR-u2iANSE")
OWNER_ID = int(getenv("OWNER_ID", "1391556668"))

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1000))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://graph.org/file/700b279c54f0d8809fccb.jpg https://graph.org/file/1412d9f93d77c350d8268.jpg')).split()
BOT_START_TIME = time()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1391556668 5162208212').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001650088903').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '2001653136').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001822021062')
auth_grp = environ.get('AUTH_GROUP', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1001139111796')
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1001831802226')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
BOT_CHANNEL_ID = int(getenv("BOT_CHANNEL_ID", "-1001822021062"))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001821439025'))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Star_Bots_Tamil_Support')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>[Star Movies Tamil](https://t.me/Star_Moviess_Tamil) - <code>{file_name}</code>\n\n🎥 Get More Movies/Series Files 📂 in [Star Movies Bot](https://t.me/Star_Moviess_Bot)\n📢 Update Channel :- [Star Movies Tamil](https://t.me/Star_Moviess_Tamil)\n🤖 Bot Channel :- [Star Bots Tamil](https://t.me/Star_Bots_Tamil)</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>🎥 Movie :- <a href={url}>{title}</a>\n\n🎭 Genres :- {genres}\n\n📆 Year :- <a href={url}/releaseinfo>{year}</a>\n\n🌟 Rating :- <a href={url}/ratings>{rating}</a> / 10 (Based on {votes} Users Ratings.)\n\n🎙️ Languages :- {languages}\n\n⏰ Duration :- {runtime} Minutes\n\n🕺 Director :- {director}\n\n🗺️ Countries :- {countries}\n\n📢 Update Channel :-</b> <a href=https://t.me/Star_Moviess_Tamil><b>Star Movies Tamil</b></a>\n\n<b>🤖 Bot Channel :- <a href=https://t.me/Star_Bots_Tamil><b></b>Star Bots Tamil</a></b>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "True"), True)
WELCOME_TEXT = environ.get("WELCOME_TEXT", "<b>Hello {mention}, Welcome to {title} Group!</b>")
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
PORT = environ.get("PORT", "8080")
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
MAX_B_TN = environ.get("MAX_B_TN", "8")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', '-1001797626445'))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), True)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

## Extra Features ##
    
      # URL Shortener #

SHORTLINK_URL = environ.get('SHORTLINK_URL', 'tnshort.net')
SHORTLINK_API = environ.get('SHORTLINK_API', 'd03a53149bf186ac74d58ff80d916f7a79ae5745')
IS_SHORTLINK = is_enabled((environ.get('IS_SHORTLINK', 'False')), False)
IS_VERIFY = is_enabled((environ.get('IS_VERIFY', 'False')), False)
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', "https://telegram.me/Star_Moviess_Bot?start=files_BAADBQAD3QwAAitd-Fb0taAQAAH02-QWBA")
VERIFY2_URL = environ.get('VERIFY2_URL', "droplink.co")
VERIFY2_API = environ.get('VERIFY2_API', "1d85e33efc4969b36e0f6c0a017aaaefd8accccc")

     # Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 300))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)

    # Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "⚡ How To Download ⚡"
DOWNLOAD_TEXT_URL = "https://telegram.me/Star_Moviess_Bot?start=files_BAADBQAD3QwAAitd-Fb0taAQAAH02-QWBA"
TUTORIAL_VIDEO = (environ.get('TUTORIAL_VIDEO', 'https://telegram.me/Star_Moviess_Bot?start=files_BAADBQAD3QwAAitd-Fb0taAQAAH02-QWBA'))

   # Custom Caption Under Button #
CAPTION_BUTTON = "🔥 Join Our Channel 🔥"
CAPTION_BUTTON_URL = "https://t.me/Star_Moviess_Tamil"

   # Auto Delete For Bot Sending Files #
FILE_DELETE_TIMER = int(environ.get('FILE_DELETE_TIMER', '3600'))

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are Enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

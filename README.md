## • What's New ?

- ⟴ URL Shortener Added
- ⟴ Self Delete Added (Auto delete)
- ⟴ Filter On Off Option Added
- ⟴ Custom Welcome Message
- ⟴ Custom Download Name And URL
- ⟴ Custom Texts (About, Help, Stats,More..)
- ⟴ Custom URL Buttons (Updates channel, Add To Group, Force Sub, More...)




<p align="center">
  <img src="https://github.com/Star-Bots-Tamil/Star-Movies-Bot/blob/main/assets/IMG_20230408_100107_995.jpg" alt="Star Bots Logo">
</p>
<h1 align="center">
  <b>Star Bots Tamil</b>
</h1>


## Features

- [x] 2GB+ Files Now Support
- [x] URL Shortener Added
- [x] Custom Buttons
- [x] Auto Filter
- [x] Manual Filter
- [x] Search in PM
- [x] IMDB
- [x] Admin Commands
- [x] Broadcast
- [x] Index
- [x] IMDB search
- [x] Inline Search
- [x] Random pics
- [x] ids and User info 
- [x] Stats, Users, Chats, Ban, Unban, Leave, Disable, Channel
- [x] Spelling Check Feature
- [x] File Store
## Variables

Read [this](https://telegram.dog/GreyMatter_Bots) before you start messing up with your edits.

### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/h9QjSSmk5tw)
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/h9QjSSmk5tw)
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.
### Optional Variables
* `PICS`: Telegraph links of images to show in start message.( Multiple images can be used separated by space )
* `FILE_STORE_CHANNEL`: Channel from were file store links of posts should be made.Separate multiple IDs by space
* Check [info.py](https://github.com/GreyMattersBot/url-auto-delete-shortener-bot/blob/main/info.py) for more
## Extra Features
* `URL_SHORTENER_WEBSITE`: URL Shortener Website Link ( Without https://)
* `URL_SHORTNER_WEBSITE_API`: URL Shortener Website API key
* `SELF_DELETE`: True if SELF_DELETE is On, False if Off
* `SELF_DELETE_SECONDS`: Enter Seconds to be SELF_DELETE 
* `START_TXT`: Enter Your Start Message
* `ABOUT_TXT`: Enter Your About Message 


## Deploy
You can deploy this bot anywhere.

<i>**[Watch Deploying Tutorial...](https://www.youtube.com/@StarBotsTamil)**</i>

<details><summary>Deploy To Heroku</summary>
<p>
<br>
<a href="https://heroku.com/deploy?template=https://github.com/Star-Bots-Tamil/Star-Movies-Bot">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>
</details>

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/GreyMattersBot/url-auto-delete-shortener-bot&branch=koyeb&name=urlshortautofilterbot)

<details><summary>Deploy To VPS</summary>
<p>
<pre>
git clone https://github.com/Star-Bots-Tamil/Star-Movies-Bot
# Install Packages
pip3 install -U -r requirements.txt
Edit info.py with variables as given below then run bot
python3 bot.py
</pre>
</p>
</details>


## Commands
```
start - Check if 😊 I'm Alive
help - How to Use❓
about - to Know About Me 😌
logs - Get The Recent Errors (Admin 👨🏻‍✈️ Only)
send - Send Message to Spacific User 🤵🏻 (Admin 👨🏻‍✈️ Only)
group_send - Send Message to Spacific Chat 🤵🏻 (Admin 👨🏻‍✈️ Only)
stats - Get Status 📊 Of Files 📂 in Database (Admin 👨🏻‍✈️ Only)
status - Get Status 📊 Of This Bot 🤖 (Admin 👨🏻‍✈️ Only)
settings - Customize Bot Settings ⚙️ (Chat Admin 👨🏻‍✈️ Only)
autofilter - On/Off Filers in a Chat (Chat Admin 👨🏻‍✈️ Only)
filter - Add a Filter in Chat
filters - List all the Filters of a Chat
gfilter - Add a Global Filter in Chat
gfilters - List all the Global Filters of a Chat
del - Delete 🗑️ a Specific Filter in Chat 
delall - Delete the Whole Filters in a Chat (Chat Admin 👨🏻‍✈️ Only)
delg - Delete 🗑️ a Specific Global Filter in Chat 
delallg - Delete the Whole Global Filters in a Chat (Chat Admin 👨🏻‍✈️ Only)
delete - Delete 🗑️ a Specific File 📂 From Database (Admin 👨🏻‍✈️ Only)
deleteall - Delete 🗑️ to All Files 📂 From Database (Admin 👨🏻‍✈️ Only)
deletefiles - Delete 🗑️ PreDVD and CAMRip Files 📂 From Database (Admin 👨🏻‍✈️ Only)
connect  - Connect a Particular Chat to Your PM
disconnect  - Disconnect From a Chat 
connections - List All Your Connections
invite - Get The Invite 💌 Link 🔗 of Any Chat Which The Bot 🤖 is Admin 👨🏻‍✈️
stickerid - Reply to Any Sticker to Get Sticker's ID
id - Get ID of a Specified User
info - Get Information About a User
imdb - Get the Movie 🎥 Information From IMDB Source
search - Get the Movie 🎥 Information from Various Sources
set_template - Set a New Custom IMDB Template For Individual Groups (Chat Admin 👨🏻‍✈️ Only)
font - Font is a Module For Make Your Text Stylish 🖊️
share - Reply with Any Text to Get Share Link 🔗
graph - Reply to a Photo or Video 🎥 Under 5MB
text2speech - Reply with Text to Get Audio Speech 💬
alive - Check Bot Alive or Not
password - Generate Secret Password 🔑
users - Get List of My Users and IDs
junk_users - Clear All Deleted Accounts & Blocked Accounts From Database
chats - Get List of The My Chats and IDs
junk_chats - Clear Admin 👨🏻‍✈️ Removed Chats or Deactivated Chats on Database
index - Add Files 📂 From a Channel
setskip - Skip Number of Messages when Indexing Files 📂
leave  - Leave From a Chat
disable  - Disable a Chat
enable - Enable a Chat
ban  - Ban a User
unban  - Unban a User
channel - Get List of Total Connected Channels
batch - Create Link 🔗 for Multiple Files 📂
link - Create Link 🔗 for One File 📂 
video - Download Video From YouTube with Any Link 🔗
song - Download Song From YouTube with Song Name 
short - Use This Command with Your Link 🔗 to Get Shorted Links 🔗
restart - Restart The Bot 🤖 With Heroku
group_broadcast - Broadcast a Message to All Groups 👥 
broadcast - Broadcast a Message to All Users 📊
```
## Support
[![telegram badge](https://img.shields.io/badge/Telegram-Group-30302f?style=flat&logo=telegram)](https://t.me/Star_Bots_Tamil_Support)
[![telegram badge](https://img.shields.io/badge/Telegram-Channel-30302f?style=flat&logo=telegram)](https://t.me/Star_Bots_Tamil)

## Thanks to 
 - Thanks To Dan For His Awesome [Library](https://github.com/pyrogram/pyrogram)
 - Thanks To [Subinps](https://github.com/subinps) for Original EvaMaria.
 - Thanks To [RushikeshNarule](https://github.com/rushikeshnarule) for Search in PM feature.
 - Thanks To All Everyone In This Journey

### Note

you a Developer.
Fork the repo and edit as per your needs.

## Inspiration
🙃

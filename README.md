<p align="center">
  <img src="https://graph.org/file/a6f99f5b71a20468b3180.jpg" alt="LuciferFilter-RoboT Logo">
</p>
<h1 align="center">
<a href="https://telegram.dog/LuciferFilter_Bot">LuciferFilter-RoboT</a>
</h1>

<p align="center">
    <img src="https://img.shields.io/github/license/PR0FESS0R-TG/LuciferFilter-RoboT?style=for-the-badge&logo=appveyor" alt="LICENSE">
    <img src="https://img.shields.io/github/contributors/PR0FESS0R-TG/LuciferFilter-RoboT?style=for-the-badge&logo=appveyor" alt="Contributors">
    <img src="https://img.shields.io/github/repo-size/PR0FESS0R-TG/LuciferFilter-RoboT?style=for-the-badge&logo=appveyor" alt="Repo Size"> <br>
    <img src="https://img.shields.io/github/issues/PR0FESS0R-TG/LuciferFilter-RoboT?style=for-the-badge&logo=appveyor" alt="Issues">
    <img src="https://img.shields.io/github/forks/PR0FESS0R-TG/LuciferFilter-RoboT?style=for-the-badge&logo=appveyor" alt="Forks">
    <img src="https://img.shields.io/github/stars/PR0FESS0R-TG/LuciferFilter-RoboT?style=for-the-badge&logo=appveyor" alt="Stars">
</p>

Best Indian Telegram AutoFilter Bot || Using Python3 Pyrogram By BIKASH 

### Credits

- Thanks to [Pyrogram](https://github.com/pyrogram/pyrogram)
- Thanks To [Zaute Km](https://gitHub.com/ZauteKm)
- Thanks To [RSR](https://github.com/RSR-TG-Info)
- Thanks To [Joelkb](https://github.com/Joelkb) 
- Thanks To [PR0FESS0R](https://github.com/PROFESS0R-TG) Who Have Edited And Modified This Repo As Now It Is (It's ME 😂)

### Support

Join Our [Telegram Group](https://t.me/Bkm_Bots_Support) For Support/Assistance And Our [Channel](https://telegram.dog/Bkm_Bots_Updates) For Updates.

Report Bugs, Give Feature Requests There..
Do Fork And Star The Repository If You Liked It.

<a href="https://telegram.dog/Bkm_Bots_Support"><img alt="telegram" src="https://img.shields.io/badge/BKM Botz Support-%22B1B17.svg?&logo=telegram&logoColor=white"></a>
<a href="https://telegram.dog/Bkm_Bots_Updates"><img alt="telegram" src="https://img.shields.io/badge/BKM Botz-%22B1B17.svg?&logo=telegram&logoColor=white"></a>

### Features

- [x] Auto Filter 
- [x] Manual Filter
- [x] IMDB
- [x] Admin Commands 
- [x] Broadcast
- [x] IMDB Search
- [x] Inline Search
- [x] Random Pics
- [x] IDs And User Info
- [x] DB Stats
- [x] Ban Users
- [x] Unban Users
- [x] Connections
- [x] Pin Message
- [x] Unpin Message 
- [x] Spelling Check Feature
- [x] File Store
- [x] Custom File Caption 
- [x] Chats Leave
- [x] Chats Disable 
- [x] DB Channel List
- [x] Chats List 
- [x] Users List
- [x] Bot PM Message 

## Variables

Read This Before You Start Messing Up With Your Edits

### Required Variables

• `ADMINS` : Username or ID of Admin. Separate multiple Admins by space

• `API_ID` : Get this value from [telegram.org](https://my.telegram.org/apps)

• `API_HASH` : Get this value from [telegram.org](https://my.telegram.org/apps)

• `BOT_TOKEN` : Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token

• `CHANNELS` : Username or ID of channel or group. Separate multiple IDs by space

• `COLLECTION_NAME` : Name of the collections. Defaults to Telegram_files. If you are using the same database, then use different collection name for each bot

• `DATABASE_NAME` : Name of the database in [mongoDB](https://www.mongodb.com/). For more help watch this [video](https://youtu.be/mD9veNL7KoE)

• `DATABASE_URL` : [mongoDB](https://www.mongodb.com/) URI. Get this value from [mongoDB](https://www.mongodb.com/). For more help watch this [video](https://youtu.be/mD9veNL7KoE)

• `AUTH_CHANNEL` : ID of channel. Without subscribing this channel users cannot use Autofilter

• `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel

### Optional Variables

• `AUTH_USERS` : Username or ID of users to give access of inline search & pm filter. Separate multiple users by space. Leave it empty if you don't want to restrict bot usage.

• `AUTH_GROUPS` : ID of groups which bot should work as autofilter, bot can only work in thease groups. If not given , bot can be used in any group.

• `PICS` : Telegraph links of images to show in start message.( Multiple images can be used separated by space )

• `IMDB` : Imdb the view of information when making True/False.

• `SINGLE_BUTTON` : Choose button single or double True/False.

• `P_TTI_SHOW_OFF` : Customize Result Buttons to Callback or Url by (True = url / False = callback).

• `FILE_STORE_CHANNEL` : Channel from were file store links of posts should be made. Separate multiple IDs by space

## Admin Commands 

```
• /alive - Check I'm Alive Or Not(All Users)
• /ping - Pong(All Users)
• /logs - To Get The Rescent Errors
• /stats - To Get Status Of Files In DataBase.(All Users)
* /filter - Add Manual Filters
* /filters - View Filters
* /connect - Connect To PM.
* /disconnect - Disconnect From PM
* /del - Delete a Filter
* /delall - Delete All Filters
* /deleteall - Delete All Index Files(Autofilter)
* /delete - Delete a Specific File From Index.
* /batch - To Create Link For Multiple Posts
* /link - To Create Link For One Post
* /info - Get User Info(All Users)
* /id - Get TG Ids.(All Users)
* /imdb - Fetch Info From IMDB Source.(All Users)
• /users - To Get List Of My Users And Ids.
• /chats - To Get List Of The My Chats And Ids 
• /index - To Add Files From a Channel
• /leave - To Leave From a Chat.
• /disable - To Disable a Chat.
* /enable - Re-Enable Chat.
• /ban_users - To Ban a User.
• /unban_users - To Unban a User.
• /channel - To Get List Of Total Connected Channels
• /broadcast - To Broadcast a Message To All Users
```

## Deployment Support Sites 

<details><summary>Deploy To Heroku</summary>
<p>
<br>
<a href="https://heroku.com/deploy?template=https://github.com/TGDragonIDM/LuciferFilter-RoboT">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy To Heroku">
</a>
</p>
</details>

<details><summary>Deploy To Koyeb</summary>
<br>
<a href="https://app.koyeb.com/deploy?type=git&repository=github.com/PR0FESS0R-TG/LuciferFilter-RoboT&branch=main&name=luciferfilterrobot">
  <img src="https://www.koyeb.com/static/images/deploy/button.svg" alt="Deploy To Koyeb">
</a>
</details>

<details><summary>Deploy To Render</summary>
<br>
<a href="https://render.com/deploy?repo=https://github.com/PR0FESS0R-TG/LuciferFilter-RoboT/tree/web">
<img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render">
</a>
</details>

<details><summary>Deploy To VPS</summary>
<p>
<pre>
git clone https://github.com/PR0FESS0R-TG/LuciferFilter-RoboT 
# Install Packages
pip3 install -U -r requirements.txt
Edit config.py with variables as given below then run bot
python3 bot.py
</pre>
</p>
</details>

## Inspiration
This Is An Attempt To Create a Clone Of a BOT Made Out Of [Benana Trees 🌳](https://telegram.dog/GetTGLink/4187)

[![For Vaza](https://telegra.ph/file/e743b0c8a04252774bac2.jpg)](https://telegra.ph/file/98342dc186fd7484cba91.mp4 "Oru Kootam Vazhakalk samarpikkunnu")

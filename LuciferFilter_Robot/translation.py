# MIT License
# Copyright (c) 2023 BIKASH

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Telegram Link : https://telegram.dog/TechProjectsUpdates 
# Repo Link : https://github.com/Pr0fess0r99/LuciferFilter-RoboT
# License Link : https://github.com/Pr0fess0r99/LuciferFilter-RoboT/blob/LuciferFilter-RoboT/LICENSE
class Script(object):
    START_TXT = """<b>👋 Hello {},

It's Power Full <a href='t.me/{username}'>{name}</a> Here 😎

Add Me To Your Group And Make Sure I'm an Admin There And Enjoy My Pever Show 😉

Maintained By ✔️ <a href='https://t.me/Pr0fess0r99'>PR0FESS0R 99</a></b>"""

    HELP_TXT = """<b>👋 Hello {},

I Can Guide You Through All Of {name}'s Cool Features & How To Properly Use Them. Use The Buttons Below To Navigate Through All Of The Modules.</b>"""

    MANUALFILTER_TXT = """Help: <b>Manual Filter</b>

- Filter Is The Feature Were Users Can Set Automated Replies For a Particular Keyword And Dingdi Will Respond Whenever a Keyword Is Found The Message 

<b>Commands and Usage:</b>
• /filter - Add a Filter In Chat.
• /filters - List All The Filters Of a Chat.
• /del - Delete a Specific Filter In Chat.
• /delall - Delete The Whole Filters In a Chat(Chat Owner Only)."""

    BUTTON_TXT = """Help: <b>Buttons</b>

- {name} Support Both Url And Alert Inline Buttons.

<b>NOTE:</b>
1. Telegram Will Not Allows You To Send Buttons Without Any Content, So Content Is Mandatory.
2. {name} Supports Buttons With Any Telegram Media Type.
3. Buttons Should Be Properly Parsed As Markdown Format.

<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/xxxxxxxxxxxxx)</code>
<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    FILLINGS_TXT = """Help: <b>Fillings</b>

- You Can Also Customize The Contents Of Your Message With Contextual Data. For Example, You Could Mention a User By Name In The Filter Message, Or Mention Them In a Filter.

<b>Supported Fillings:</b>
- <code>{first}</code>: The user's first name.
- <code>{last}</code>: The user's last name.
- <code{username}</code>: The user's username.
- <code>{mention}</code>: Mentions the user with their firstname.
- <code>{id}</code>: The user's ID.
- <code>{dcid}</code>: The user's DC ID.
- <code>{chatname}</code>: The chat's name.
- <code>{query}</code>: Any Replied Message.

<b>Example:</b> <code>/filter Test Hello {mention} This Is Your Username : {username} And This Is Your ID : {id}</code>"""

    CONNECTION_TXT = """Help: <b>Group Connections</b>

- Used To Connect Bot To PM For Managing Filters. 
- It Helps To Avoid Spamming In Groups.

<b>NOTE:</b>
1. Only Admins Can Add a Connection.
2. Send <code>/connect</code> For Connecting Me To Your PM.

<b>Commands and Usage:</b>
• /connect  - Connect a Particular Chat To Your PM.
• /disconnect  - Disconnect From a chyat.
• /connections - List All Your Connections."""

    AUTO_MANUAL_TXT = """Help: <b>Filters</b>

<b>Select a Filters Type Bellow.</b>"""
  
    TGRAPH_TXT = """Help: <b>TGraph</b>

- Do As You Wish With Telegra.ph Module..!

<b>Commands and Usage:</b>
• /telegraph and /tgmedia or /tgraph - Upload Supported Media (Within 5MB) To Telegraph.

<b>NOTE:</b>
• {name} Should Have Admin Privillage.
• These Commands Works On Both PM And Group.
• These Commands Can Be Used By Any Member."""

    INFO_TXT = """Help: <b>Information</b>

- Get Information About Something..!

<b>Commands and Usage:</b>
• /id - Get ID Of a Specified User.
• /info  - Get Information About a User.
• /json - Get The JSON Details Of a Message.

<b>NOTE:</b>
• {name} Should Have Admin Privillage.
• These Commands Works On Both PM And Group.
• These Commands Can Be Used By Any Member."""

    GTRANS_TXT = """Help: <b>Google Translator</b>

- Translate Texts To a Specific Language..!

<b>Commands and Usage:</b>
• /tr [language code][reply] - Translate Replied Message To Specific Language.

<b>NOTE:</b>
• {name} Should Have Admin Privillage.
• These Commands Works On Both PM And Group.
• {name} Can Translate Texts To 200+ Languages."""

    SEARCH_TXT = """Help: <b>IMDB</b>

- Search Many Things Without Leaving Telegram..!

<b>Commands and Usage:</b>
• /imdb  - Get The Film Information From IMDB Source.
• /search  - Get The Film Information From Various Sources.

<b>NOTE:</b>
• {name} Should Have Admin Privillage.
• More Search Tools Can Be Found On Inline.
• These Commands Works On Both PM And Group."""

    PURGE_TXT = """Help: <b>Purge</b>

- You Need To Delete Lots Of Messages..? That's What Purges Are For..!

<b>Commands and Usage:</b>
• /purge - Delete All Messages From The Replied To Message, To The Current Message.

<b>NOTE:</b>
• {name} Should Have Admin Privillage.
• These Commands Works On Group.
• These Commands Can Be Used By Admin Only."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>

- Some People Need To Be Publicly Banned Spammers, Annoyances Or Just Trolls.
- This Module Allows You To Do That Easily, By Exposing Some Common Actions, So Everyone Will See..!

<b>Commands and Usage:</b>
• /ban - Ban a User.
• /tban - Temporarily Ban a User. Example Time Values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /mute - Mute a User.
• /tmute - Temporarily Mute a User. Example Time Values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /unban or /unmute - Unmute a User & Unban a User.

<b>Examples:</b>
- Mute a User For Two Hours.
- <code>/tmute @username 2h</code>

<b>NOTE:</b>
• {name} Should Have Admin Privillage.
• These Commands Works On Group.
• These Commands Can Be Used By Admin Only."""

    PIN_MESSAGE_TXT = """Help: <b>Pin Message</b>

- All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With a Simple Pinned Message..!

<b>Commands and Usage:</b>
• /pin: Pin The Message You Replied To. Add 'loud' Or 'notify' To Send a Notification To All Group Members.
• /unpin: Unpin The Current Pinned Message. If Used As a Reply, Unpins The Replied To Message.

<b>NOTE:</b>
• {name} Should Have Admin Privillage.
• These Commands Works Only Group.
• These Commands Can Be Used By Admin Only."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
• This Module Only Works For My Admins 

<b>Commands and Usage:</b>
• /logs - To Get The Rescent Errors.
• /stats - To Get Status Of Files In DataBase.
• /delete - To Delete a Specific File From DataBase.
• /users - To Get List Of My Users And IDs.
• /chats - To Get List Of The My Chats And IDs.
• /leave - To Leave From a Chat.
• /disable - To Disable a Chat.
• /ban_users - To Ban a User.
• /unban_users - To Unban a User.
• /channel - To Get List Of Total Connected Channels.
• /broadcast - To Broadcast a Message To All Users."""
 
    WHO_TXT = """Hello 👋 {},
I Can't Write Everything In My Bio So I Created This...

╭──[─═ ᴘᴇʀꜱᴏɴᴀʟ ɪɴꜰᴏ ═─]
├• Name⇝ Bikash Maity 
├• Gender⇝ What Do You Think
├• TG Name⇝ PR0FESS0R 99 
├• Username⇝ @Pr0fess0r99
├• Birthday⇝ 10th January 2006
├• Age⇝ 17
├• Relationship Status⇝ Single
├• Nationality⇝ Indian
├• Location⇝ West Bengal, India, Manikpur 
├• Contact Bot⇝ Soon... 🤖
╰──────⍟───────╯

Thank You For Reading Patiently 🙏"""


    DONATE_TXT = """Hello 👋 {},

To Support My Works, Please Feel Free To Donate Any Amount You Like 💸

There Are Multiple Ways To Donate By UPI ID

UPI 🆔 Details

Google pay 📲 joynathnet4@oksbi
Phonepe 📲 bijoy.nath@ybl

Thank You For Showing Interest In My Works 🙏"""

    SONG_TXT = """Help: <b>Song</b>

- Download Music Via Link, For Those Who Love Music

<b>Commands and Usage:</b>
• /song [Song Name] or /song [YouTube Link] - To Download Music"""
  
    FONT_TXT = """Help: <b>Stylish Font</b>

- Generate Stylish Text With Your Own Writing

<b>Commands and Usage:</b>
• /font [Text] - Generate Your Stylish Text"""

    STATUS_TXT = """<b>Total Files:</b> <code>{}</code>
<b>Total Users:</b> <code>{}</code>
<b>Total Chats:</b> <code>{}</code>
<b>Used Storage:</b> <code>{}</code> MiB
<b>Free Storage:</b> <code>{}</code> MiB"""

    FORCESUB_TXT = """**♦️ READ THIS INSTRUCTION ♦️**

__🗣 In Order To Get The Movie Requested By You In Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately 🙈__

**👇 SUBSCRIBE CHANNEL & TRY AGAIN 👇**"""
   
    CUSTOM_FILE_CAPTION = """<code>{file_name}</code>"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    CREATOR_REQUIRED = """You Have To Be The Group Creator To Do That❗"""
      
    INPUT_REQUIRED = "**Arguments Required❗**"
      
    KICKED = """Successfully Kicked {} Members According To The Arguments Provided ☑️"""
      
    START_KICK = """Removing Inactive Members This May Take a While 🚮"""
      
    ADMIN_REQUIRED = """I Am Not An Admin Here\n__Leaving This Chat, Add Me Again As Admin With Ban User Permission."""
      
    DKICK = """Kicked {} Deleted Accounts Successfully ☑️"""
      
    FETCHING_INFO = """Collecting Users Information"""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}"""

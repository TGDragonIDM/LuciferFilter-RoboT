from __future__ import unicode_literals

import os, requests, asyncio, math, time, wget
from pyrogram import filters, Client
from pyrogram.types import Message

from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL


@Client.on_message(filters.command(['song', 'mp3']) & filters.private)
async def song(client, message):
    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = await message.reply(f"**Searching Your Song...!\n {query}**")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)
        performer = f"[PR0FESS0R]" 
        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]
    except Exception as e:
        print(str(e))
        return await m.edit("**𝙵𝙾𝚄𝙽𝙳 𝙽𝙾𝚃𝙷𝙸𝙽𝙶 𝙿𝙻𝙴𝙰𝚂𝙴 𝙲𝙾𝚁𝚁𝙴𝙲𝚃 𝚃𝙷𝙴 𝚂𝙿𝙴𝙻𝙻𝙸𝙽𝙶 𝙾𝚁 𝙲𝙷𝙴𝙲𝙺 𝚃𝙷𝙴 𝙻𝙸𝙽𝙺**")
                
    await m.edit("**Downloading Your Song...!**")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)

        cap = "**Uploaded By: <a href='https://t.me/Pr0fess0r99'>PR0FESS0R 99</a>**"
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        await message.reply_audio(
            audio_file,
            caption=cap,            
            quote=False,
            title=title,
            duration=dur,
            performer=performer,
            thumb=thumb_name
        )            
        await m.delete()
    except Exception as e:
        await m.edit("**🚫 𝙴𝚁𝚁𝙾𝚁 🚫**")
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

def get_text(message: Message) -> [None,str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " not in text_to_return:
        return None
    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        return None

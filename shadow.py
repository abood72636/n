
import re
import base64
import asyncio
import logging
from telethon import events
from config import *
from asyncio import sleep
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger("𝐀𝐛𝐨𝐨𝐝")
logger.info("النشر التلقائي شغال الان استمتع ✓")

anti = False
async def aljoker_nshr(shadow, sleeptimet, chat, message, seconds):
    global anti
    anti = True
    while anti:
        if message.media:
            sent_message = await shadow.send_file(chat, message.media, caption=message.text)
        else:
            sent_message = await shadow.send_message(chat, message.text)
        await asyncio.sleep(sleeptimet)
@shadow.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر (\d+) (@?\S+)$"))
async def Hussein(event):
    await event.delete()
    parameters = re.split(r'\s+', event.text.strip(), maxsplit=2)
    if len(parameters) != 3:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    seconds = int(parameters[1])
    chat_usernames = parameters[2].split()
    shadow = event.client
    global anti
    anti = True
    message = await event.get_reply_message()
    for chat_username in chat_usernames:
        try:
            chat = await shadow.get_entity(chat_username)
            await aljoker_nshr(shadow, seconds, chat.id, message, seconds)  # تمرير قيمة seconds هنا لكل مجموعة
        except Exception as e:
            await event.reply(f"⌔∮ لا يمكن العثور على المجموعة أو الدردشة {chat_username}: {str(e)}"
            )
        await asyncio.sleep(1)

    
async def aljoker_allnshr(shadow, sleeptimet, message):
    global anti
    anti = True
    aljoker_chats = await shadow.get_dialogs()
    while anti:
        for chat in aljoker_chats:
            if chat.is_group:
                try:
                    if message.media:
                        await shadow.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await shadow.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@shadow.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر_كروبات (\d+)$"))
async def Hussein(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    shadow = event.client
    global anti
    anti = True
    await aljoker_allnshr(shadow, sleeptimet, message)

super_groups = ["super", "سوبر"]
async def aljoker_supernshr(shadow, sleeptimet, message):
    global anti
    anti = True
    aljoker_chats = await shadow.get_dialogs()
    while anti:
        for chat in aljoker_chats:
            chat_title_lower = chat.title.lower()
            if chat.is_group and any(keyword in chat_title_lower for keyword in super_groups):
                try:
                    if message.media:
                        await shadow.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await shadow.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@shadow.on(events.NewMessage(outgoing=True, pattern=r"^\.سوبر (\d+)$"))
async def Hussein(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    shadow = event.client
    global anti
    anti = True
    await aljoker_supernshr(shadow, sleeptimet, message)

@shadow.on(events.NewMessage(outgoing=True, pattern='.ايقاف النشر'))
async def stop_aljoker(event):
    global anti
    anti = False
    await event.edit("**᯽︙ تم ايقاف النشر التلقائي بنجاح ✓** ")
@shadow.on(events.NewMessage(outgoing=True, pattern=r"^\.(الاوامر|فحص)$"))
async def Hussein(event):
    await event.delete()
    if event.pattern_match.group(1) == "الاوامر":
        joker_313 = """**
🔰 قـائمة اوامر النشر التلقائي للمجموعات

===== 𝐀𝐛𝐨𝐨𝐝 =====

`.نشر` عدد الثواني معرف الكروب :
 - للنشر في المجموعة التي وضعت معرفها مع عدد الثواني

`.نشر_كروبات` عدد الثواني : 
- للنشر في جميع المجموعات الموجوده في حسابك
 
`.سوبر` عدد الثواني : 
- للنشر بكافة المجموعات السوبر التي منظم اليها 

`.ايقاف النشر` :
- لأيقاف جميع انواع النشر اعلاه

• مُـلاحظة : جميع الأوامر اعلاه تستخدم بالرد على الرسالة او الكليشة المُراد نشرها

===== 𝐀𝐛𝐨𝐨𝐝 =====
    **"""
        await event.reply(file='https://telegra.ph/file/7032a5d686f3c7695379b.jpg', message=joker_313)
    elif event.pattern_match.group(1) == "فحص":
        hussein_ali = "**• بوت النشر يعمل بنجاح √\n• المطور : @C_N_i**"
        await event.reply(file='https://telegra.ph/file/7032a5d686f3c7695379b.jpg', message=hussein_ali)


@shadow.on(events.NewMessage(outgoing=True, pattern=r"\.قلب"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "❤️", "🖤", "💜", "🖕", "💛", "💚", "💙"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])

@shadow.on(events.NewMessage(outgoing=True, pattern=r"\.قلوب"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "❤️",
        "❤️🖤",
        "❤️🖤💜",
        "❤️🖤💜🧡",
        "❤️🖤💜🧡💛",
        "❤️🖤💜🧡💛💚",
        "❤️🖤💜🧡💛💚💙",
        "❤️🖤💜🧡💛💚",
        "❤️🖤💜🧡💛",
        "❤️🖤💜🧡",
        "❤️🖤💜",
        "❤️🖤",
        "💓"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17])

print('تم تشغيل بوت النشر التلقائي  ')
shadow.run_until_disconnected()




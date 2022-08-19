# code by Asad Ali Owner Off Jankari Ki Duniya Youtube Channel


import os
import sys
import asyncio
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config import bot, call_py, HNDLR, contact_filter
from time import time
from datetime import datetime

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Week", 60 * 60 * 24 * 7),
    ("Day", 60 * 60 * 24),
    ("Hour", 60 * 60),
    ("Min", 60),
    ("Sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(contact_filter & filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("`pinging...`")
    delta_ping = time() - start
    await m_reply.edit("0% ▒▒▒▒▒▒▒▒▒▒")
    await m_reply.edit("20% ██▒▒▒▒▒▒▒▒")
    await m_reply.edit("40% ████▒▒▒▒▒▒")
    await m_reply.edit("60% ██████▒▒▒▒")
    await m_reply.edit("80% ████████▒▒")
    await m_reply.edit("100% ██████████")
    end = datetime.now()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(f"**┞◈𝗣𝗼𝗻𝗴!! Music Userbot🏓**\n**┞◈Pinger - {delta_ping * 1000:.3f} ms \n**Uptime ⏳** - {uptime}")


@Client.on_message(contact_filter & filters.command(["restart"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
    await m.reply("`Memulai Ulang...`")
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@Client.on_message(contact_filter & filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    HELP = f"""
👋 Hallo {m.from_user.mention}!
🛠 MENU BANTUAN EIKO MUSIC PLAYER 🛠

⚡ PERINTAH UNTUK SEMUA ORANG

• {HNDLR}play [judul lagu | link youtube | balas file audio] - untuk memutar lagu
• {HNDLR}vplay [judul video | link youtube | balas file video] - untuk memutar video
• {HNDLR}playlist untuk melihat daftar putar
• {HNDLR}ping - untuk cek status
• {HNDLR}stream untuk memainkan livestreaming radio
• {HNDLR}vstream untuk link livestreaming
• {HNDLR}id - untuk melihat id pengguna
• {HNDLR}video - judul video | link yt untuk mencari video
• {HNDLR}song - judul lagu | link yt untuk mencari lagu
• {HNDLR}help - untuk melihat daftar perintah
• {HNDLR}join- untuk join | ke grup 
• {HNDLR}resume - untuk melanjutkan pemutaran lagu atau video
• {HNDLR}pause - untuk untuk menjeda pemutaran lagu atau video
• {HNDLR}skip - untuk melewati lagu atau video (Khusus Perintah ini sudah bisa untuk semua) 
• {HNDLR}end - untuk mengakhiri pemutaran
• {HNDLR}restart - memulai ulang bot

👩🏻‍💻 Dibuat Oleh Az ✨
""" 
    await m.reply(HELP)


@Client.on_message(contact_filter & filters.command(["repo"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    REPO = f"**🛠 Jika kamu mau reponya 🛠** \n\n**Hubungi ** [Az](t.me/tth_kiya98)\n**Jika kamu menyukainya silahkan** Gunakan [Bot Management](t.me/EikoManager_Bot) Untuk Mengatur grupmu dan cek [Update](t.me/CatatanAz) dan juga [Gabung](t.me/CatatanAzDay)"
    await m.reply(REPO)

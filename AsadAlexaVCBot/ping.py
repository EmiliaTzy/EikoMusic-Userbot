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
    m_reply = await m.reply_text("`...`")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(f"`{delta_ping * 1000:.3f} ms` \n**Uptime ⏳** - `{uptime}`")


@Client.on_message(contact_filter & filters.command(["restart"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
    await m.reply("`Restarting...`")
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@Client.on_message(contact_filter & filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    HELP = f"**🛠 Menu bantuan 🛠** \n\n**Siapa pun dapat menggunakan perintah ini jika mode grup disetel ke true**\n**untuk memainkan lagu** {HNDLR}play\n** untuk memainkan lagu dalam video** {HNDLR}vplay\n**untuk radio livestreaming** {HNDLR}stream (**untuk link radio**) \n**untuk link live** {HNDLR}vstream (untuk .m3u8 / link live) \n\n**PERINTAH SUDO** (**Anda dapat menjalankan perintah ini jika Anda berada di daftar kontak saya, hubungi pemilik saya** @tth_kiya98 **Untuk menjadi sudo**): \n**untuk mengecek ping** {HNDLR}ping \n**Melewati Lagu** {HNDLR}skip \n**Untuk Menjeda Lagu Yang Sedang Dimainkan** {HNDLR}pause Dan **Untuk Melanjutkan Lagu Yang Dimainkan **{HNDLR}resume \n**Untuk Menghentikan Lagu** {HNDLR}stop / **Untuk Mengakhiri Lagu** {HNDLR}end \n**Untuk Menu Bantuan** {HNDLR}help \n**Untuk Mendapatkan Repo** {HNDLR}repo \n**Untuk Memulai Ulang Bot** {HNDLR}restart"
    await m.reply(HELP)


@Client.on_message(contact_filter & filters.command(["repo"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    REPO = f"**🛠 Jika kamu mau reponya 🛠** \n\n**Hubungi ke** [Az](t.me/tth_kiya98)\n**Jika kamu menyukainya silahkan ** [Bot Management](t.me/EikoManager_Bot) [Update](t.me/CatatanAz) [Gabung](t.me/CatatanAzDay)"
    await m.reply(RE** [Bot Management](t.me/EikoManager_Bot) [Update](t.me/CatatanAz) [Gabung](t.me/CatatanAzDay)"
    await m.reply(REPO)PO)

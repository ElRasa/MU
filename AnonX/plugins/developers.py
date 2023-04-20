import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

#          
                
@app.on_message(
    command(["المبرمج","رسام","مطور السورس","مبرمج السورس"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/74bf3bd702a30b8912d7c.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𓏺 𝙀𝙇𝙍𝘼𝙎𝘼𝙈 ‌𝅘𝅥𝅯 ˼](https://t.me/Mahmod777777)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @Mahmod777777 ❫
◉ 𝙸𝙳      : ❪ 2125600195 ❫
◉ 𝙱𝙸𝙾    : ❪{لاتحزن إن الله معنا}❤️{ @Osman_yy }{ @E_L_R_A_S_A_M }⚡⌠ @Ve_m1 ⌡❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝙀𝙇𝙍𝘼𝙎𝘼𝙈 ‌𝅘𝅥𝅯", url=f"https://t.me/Mahmod777777"), 
                 ],[
                   InlineKeyboardButton(
                        "⌞ 𝅘𝅥𝅯𝙎𝙊𝙐𝙍𝘾𝙀 𝙑𝙀𝙉𝙊𝙈 𝅘𝅥𝅯 ⌝", url=f"https://t.me/Ve_m1"),
                ],

            ]

        ),

    )

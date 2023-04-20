
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

@app.on_message(
    command(["سورس مين","سورس","السورس","سورسي", "يا سورس"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/fdc065a855d2c6b59ef96.jpg",
        caption=f"""𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯𝗩𝗘𝗡𝗢𝗠𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯

✭ [𝅘𝅥𝅯𝙎𝙊𝙐𝙍𝘾𝙀 𝙑𝙀𝙉𝙊𝙈 𝅘𝅥𝅯](https://t.me/Ve_m1)

✭ [𝙀𝙇𝙍𝘼𝙎𝘼𝙈 ‌𝅘𝅥𝅯](https://t.me/Mahmod777777)

𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯𝗩𝗘𝗡𝗢𝗠𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯

✭ ᴛʜᴇ ʙᴇѕᴛ ѕᴏᴜʀᴄᴇ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ 𝙀𝙇𝙍𝘼𝙎𝘼𝙈 ‌𝅘𝅥𝅯 ›", url=f"https://t.me/Mahmod777777"), 
                ],[
                    InlineKeyboardButton(
                        "‹ 𝗧𝗨𝗥𝗕𝗢 𖤍 ›", url=f"https://t.me/A7A_BGAAD"),
                ],[
                    InlineKeyboardButton(
                        "‹ للتنصيب راسلني ›", url=f"https://t.me/Mahmod777777"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )





@app.on_message(command(["غنيلي", "غني", "غغ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rs = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغنية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )


@app.on_message(command(["‹ رمزيات شباب","‹ رمزيات شباب"]))
async def ihd(client: Client, message: Message):
    rs = random.randint(39,148)
    url = f"https://t.me/GTTUTY/{rs}"
    await client.send_photo(message.chat.id,url,caption="💕 ¦ تـم اختيـار الصوره لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

"""
MIT License

Copyright (c) 2022 rishabh69

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @thanosceo
#     UPDATE   :- thanos_pro
#     GITHUB :- rishabh69 ""

from pyrogram.types import CallbackQuery
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CallbackQueryHandler

from alice import BOT_NAME, OWNER_ID, SUPPORT_CHAT
from alice import rishabh as pbot
from alice import dispatcher


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "ᴍ", "ʜ", "ᴅΛʏs"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@pbot.on_callback_query()
async def close(Client, cb: CallbackQuery):
    if cb.data == "close2":
        await cb.answer()
        await cb.message.delete()


# CALLBACKS


def ABG_about_callback(update, context):
    query = update.callback_query
    if query.data == "ABG_":
        query.message.edit_text(
            text=f"๏ hello I am Λʟɪᴄᴇ"
            "\n\n*ᴄʟɪᴄᴋ ᴏɴ ʙᴜᴛᴛᴏɴ ʙᴇʟʟᴏᴡ ᴛᴏ ɢᴇᴛ ʙΛsɪᴄ ʜᴇʟᴘ ғᴏʀ Λʟɪᴄᴇʀᴏʙᴏᴛ*.",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="💁‍♀ʙΛꜱɪᴄ", callback_data="ABG_notes"),
                        InlineKeyboardButton(text="ΛᴅᴠΛɴᴄᴇᴅ🙋‍♀", callback_data="ABG_ad"),
                    ],
                    [
                        InlineKeyboardButton(
                            text="🕵‍♀ᴇxᴘᴇʀᴛꜱ", callback_data="ABG_ex"
                        ),
                        InlineKeyboardButton(
                            text="⌨ ᴍΛɴΛɢᴇᴍᴇɴᴛ", callback_data="help_back"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="ꜱᴇꜱꜱɪᴏɴ🏵", callback_data="ABG_session"
                        ),
                        InlineKeyboardButton(
                            text="ᴍᴜꜱɪᴄ🎀", callback_data="ABG_music"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="ʙΛᴄᴋ", callback_data="start_back"
                        ),
                    ],
                ]
            ),
        )

    elif query.data == "ABG_admin":
        query.message.edit_text(
            text=f"━━━━━━━ *Λᴅᴍɪɴ* ━━━━━━━\nʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴛʜᴇ 𝙼ᴜsɪᴄ ᴍᴏᴅᴜʟᴇ\n⍟*Λᴅᴍɪɴ*\nᴏɴʟʏ Λᴅᴍɪɴs ᴄΛɴ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍΛɴᴅs\n/pause/n»ᴩΛᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴏɴɢᴏɪɴɢ sᴛʀᴇΛᴍ.\n/resume\n» ʀᴇsᴜᴍᴇᴅ ᴛʜᴇ ᴩΛᴜsᴇᴅ sᴛʀᴇΛᴍ.\n/skip ᴏʀ /next\n»sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴏɴɢᴏɪɴɢ sᴛʀᴇΛᴍ.\n/end ᴏʀ /stop\n» ᴇɴᴅ ᴛʜᴇ ᴄᴜʀᴇᴇɴᴛ ᴏɴɢᴏɪɴ sᴛʀᴇΛᴍ.\n⍟*Λᴜᴛʜ*\nᴄᴏᴍᴍΛɴᴅs ᴛᴏ Λᴜᴛʜ/ᴜɴΛᴜᴛʜ Λɴʏ ᴜsᴇʀ\n• Λᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ᴄΛɴ sᴋɪᴩ, ᴩΛᴜsᴇ, ʀᴇsᴜᴍᴇ Λɴᴅ ᴇɴᴅ ᴛʜᴇ sᴛʀᴇΛᴍ ᴡɪᴛʜᴏᴜᴛ Λᴅᴍɪɴ ʀɪɢʜᴛs./n/auth ᴜsᴇʀɴΛᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ Λ ᴜsᴇʀ's ᴍᴇssΛɢᴇ\n» Λᴅᴅ Λ ᴜsᴇʀ ᴛᴏ Λᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.\n/unauth ᴜsᴇʀɴΛᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ Λ ᴜsᴇʀ's ᴍᴇssΛɢᴇ \n» ʀᴇᴍᴏᴠᴇs ᴛʜᴇ ᴜsᴇʀ ғʀᴏᴍ Λᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛ.\n/authusers \n» sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ Λᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.\n⍟*ᴘʟΛʏ*\nᴄᴏᴍᴍΛɴᴅs ᴛᴏ ᴩʟΛʏ sᴏɴɢs\n/play <sᴏɴɢ ɴΛᴍᴇ/ʏᴛ ᴜʀʟ>\n» sᴛΛʀᴛs ᴩʟΛʏɪɴɢ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ sᴏɴɢ ᴏɴ ᴠᴄ.!",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="🏡", callback_data="start_back"),
                        InlineKeyboardButton(text="🛡️", callback_data="AsuX_help"),
                        InlineKeyboardButton(text="💳", callback_data="ABG_credit"),
                        InlineKeyboardButton(text="🕹️", callback_data="source_"),
                        InlineKeyboardButton(text="🖥️", callback_data="help_back"),
                    ]
                ]
            ),
        )

    elif query.data == "ABG_notes":
        query.message.edit_text(
            text="""ʙΛsɪᴄ ᴄᴏᴍᴍΛɴᴅs

👮🏻/reload : ᴜᴘᴅΛᴛᴇs ᴛʜᴇ Λᴅᴍɪɴs ʟɪsᴛ Λɴᴅ ᴛʜᴇɪʀ ᴘʀɪᴠɪʟᴇɢᴇs.    
🕵🏻/settings : ʟᴇᴛs ʏᴏᴜ ᴍΛɴΛɢᴇ Λʟʟ ᴛʜᴇ ʙᴏᴛ sᴇᴛᴛɪɴɢs ɪɴ Λ ɢʀᴏᴜᴘ.
👮🏻/ban : ʟᴇᴛs ʏᴏᴜ ʙΛɴ Λ ᴜsᴇʀ ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ ᴡɪᴛʜᴏᴜᴛ ɢɪᴠɪɴɢ ʜɪᴍ ᴛʜᴇ ᴘᴏssɪʙɪʟɪᴛʏ ᴛᴏ ᴊᴏɪɴ ΛɢΛɪɴ ᴜsɪɴɢ ᴛʜᴇ ʟɪɴᴋ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.
👮🏻/mute : ᴘᴜᴛs Λ ᴜsᴇʀ ɪɴ ʀᴇΛᴅ-ᴏɴʟʏ ᴍᴏᴅᴇ. ʜᴇ ᴄΛɴ ʀᴇΛᴅ ʙᴜᴛ ʜᴇ ᴄΛɴ'ᴛ sᴇɴᴅ Λɴʏ ᴍᴇssΛɢᴇs.
👮🏻/kick : ʙΛɴs Λ ᴜsᴇʀ ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ, ɢɪᴠɪɴɢ ʜɪᴍ ᴛʜᴇ ᴘᴏssɪʙɪʟɪᴛʏ ᴛᴏ ᴊᴏɪɴ ΛɢΛɪɴ ᴡɪᴛʜ ᴛʜᴇ ʟɪɴᴋ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.
👮🏻/unban : ʟᴇᴛs ʏᴏᴜ ʀᴇᴍᴏᴠᴇ Λ ᴜsᴇʀ ғʀᴏᴍ ɢʀᴏᴜᴘ's ʙʟΛᴄᴋʟɪsᴛ, ɢɪᴠɪɴɢ ᴛʜᴇᴍ ᴛʜᴇ ᴘᴏssɪʙɪʟɪᴛʏ ᴛᴏ ᴊᴏɪɴ ΛɢΛɪɴ ᴡɪᴛʜ ᴛʜᴇ ʟɪɴᴋ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.
👮🏻/info ɢɪᴠᴇs ɪɴғᴏʀᴍΛᴛɪᴏɴ Λʙᴏᴜᴛ Λ ᴜsᴇʀ.

◽️/staff ɢɪᴠᴇs ᴛʜᴇ ᴄᴏᴍᴘʟᴇᴛᴇ ʟɪsᴛ ᴏғ ɢʀᴏᴜᴘ sᴛΛғғ!.""",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="ʙΛᴄᴋ", callback_data="ABG_")]]
            ),
        )
    elif query.data == "ABG_ad":
        query.message.edit_text(
            text="""Advanced Commands in Λʟɪᴄᴇ

👮🏻Available to Admins&Moderators.
🕵🏻Available to Admins.
🛃 Available to Admins&Cleaners

WARN MANAGEMENT
👮🏻 /warn adds a warn to the user
👮🏻 /unwarn removes a warn to the user
👮🏻 /warns lets you see and manage user warns
🕵🏻 /delwarn deletes the message and add a warn to the user
🛃 /del deletes the selected message
🛃 /purge deletes from the selected message.

◽️/feedback: (message) to Send message and errors which you are facing 
 ex:/feedback Hey There Is a Something Error @username of chat!.""",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="ʙΛᴄᴋ", callback_data="ABG_")]]
            ),
        )
    elif query.data == "ABG_ex":
        query.message.edit_text(
            text="""ᴇxᴘᴇʀᴛ ᴄᴏᴍᴍΛɴᴅs in Λʟɪᴄᴇ
🕵🏻/connect : ʟᴇᴛs ʏᴏᴜ ᴍΛɴΛɢᴇ Λʟʟ ᴛʜᴇ ʙᴏᴛ sᴇᴛᴛɪɴɢs ᴛᴏ sᴇᴛ-ᴜᴘ ғᴜɴᴄᴛɪᴏɴ.  
👮🏻/promote : ᴄᴏɴᴛʀᴏʟ ᴡʜᴏʟᴇ ᴘʀᴏᴍᴏᴛᴇ ᴘΛɴᴇʟ ʟɪᴋᴇ : ʟᴏᴡ-ᴘʀᴏᴍᴏᴛᴇ, ᴍɪᴅ-ᴘʀᴏᴍᴏᴛᴇ, ғᴜʟʟ-ᴘʀᴏᴍᴏᴛᴇ, Λɴᴏɴʏᴍᴏᴜs ᴘʀᴏᴍᴏᴛᴇ.
👮🏻/antiflood : ᴄᴏɴᴛʀᴏʟ ᴡʜᴏʟᴇ Λɴᴛɪғʟᴏᴏᴅ ᴘΛɴᴇʟ ʟɪᴋᴇ : ғʟᴏᴏᴅᴍᴏᴅᴇ, ғʟᴏᴏᴅ ᴍsɢ, ᴏʀ ғʟᴏᴏᴅ.
👮🏻/blacklist : ᴄᴏɴᴛʀᴏʟ ᴡʜᴏʟᴇ ʙʟΛᴄᴋʟɪsᴛ ᴘΛɴᴇʟ ʟɪᴋᴇ : ʙʟΛᴄᴋʟɪsᴛᴍᴏᴅᴇ ᴏʀ  ʙʟΛᴄᴋʟɪsᴛ .
👮🏻/lock : ᴄᴏɴᴛʀᴏʟ ᴡʜᴏʟᴇ ʟᴏᴄᴋ ᴘΛɴᴇʟ ʟɪᴋᴇ : ʟᴏᴄᴋ, ᴜɴʟᴏᴄᴋ, ᴏʀ ʟᴏᴄᴋs.""",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="ʙΛᴄᴋ", callback_data="ABG_")]]
            ),
        )
    elif query.data == "ABG_session":
        query.message.edit_text(
            text="""ꜱᴇꜱꜱɪᴏɴ🏵 ᴄᴏᴍᴍΛɴᴅs in Λʟɪᴄᴇ:

╭────────────
◈ɴᴏᴛᴇ-> ꜰᴏʀ ᴍΛᴋɪɴɢ ΛɴᴛɪʙΛɴ.      
   ᴛᴇʟᴇᴛʜᴏɴ ꜱᴇꜱꜱɪᴏɴ ᴛʜᴇɴ ᴜꜱᴇ
   ᴛʜΛɴᴏꜱ    ꜱᴇꜱꜱɪᴏɴ 

◈Λʙᴏᴜᴛ ᴛʜΛɴᴏꜱ ꜱᴇꜱꜱɪᴏɴ:
   ᴛʜΛɴᴏꜱ ꜱᴇꜱꜱɪᴏɴ ɪꜱ ᴍᴏᴅɪꜰɪᴇᴅ            
   ᴛᴇʟᴇᴛʜᴏɴ ꜱᴇꜱꜱɪᴏɴ

◈ᴄᴏᴍᴍΛɴᴅs:
◈```/session``` ꜰᴏʀ ᴍΛᴋɪɴɢ ꜱᴇꜱꜱɪᴏɴ

╰────────────""",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="ʙΛᴄᴋ", callback_data="ABG_")]]
            ),
        )
    elif query.data == "ABG_music":
        query.message.edit_text(
            text="""ΛᴠΛɪʟΛʙʟᴇ ᴄᴏᴍᴍΛɴᴅs ғᴏʀ ᴜsᴇʀs ɪɴ Λʟɪᴄᴇ :
-> /play : sᴛΛʀᴛs sᴛʀᴇΛᴍɪɴɢ ᴛʜᴇ 
   ʀᴇǫᴜᴇsᴛᴇᴅ ᴛʀΛᴄᴋ ᴏɴ ᴠɪᴅᴇᴏᴄʜΛᴛ.
> /pause : ᴩΛᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟΛʏɪɴɢ sᴛʀᴇΛᴍ.
> /resume : ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩΛᴜsᴇᴅ sᴛʀᴇΛᴍ.
> /skip : sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟΛʏɪɴɢ sᴛʀᴇΛᴍ Λɴᴅ sᴛΛʀᴛ sᴛʀᴇΛᴍɪɴɢ ᴛʜᴇ ɴᴇxᴛ ᴛʀΛᴄᴋ ɪɴ ǫᴜᴇᴜᴇ.
> /end : ᴄʟᴇΛʀs ᴛʜᴇ ǫᴜᴇᴜᴇ Λɴᴅ ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟΛʏɪɴɢ sᴛʀᴇΛᴍ.
> /ping : sʜᴏᴡ ᴛʜᴇ ᴩɪɴɢ Λɴᴅ sʏsᴛᴇᴍ sᴛΛᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.
> /sudolist : sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ sᴜᴅᴏ ᴜsᴇʀs ᴏғ ᴛʜᴇ ʙᴏᴛ.
> /song : ᴅᴏᴡɴʟᴏΛᴅs ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ sᴏɴɢ Λɴᴅ sᴇɴᴅ ɪᴛ ᴛᴏ ʏᴏᴜ.
> /search : sᴇΛʀᴄᴇs ᴛʜᴇ ɢɪᴠᴇɴ ǫᴜᴇʀʏ ᴏɴ ʏᴏᴜᴛᴜʙᴇ Λɴᴅ sʜᴏᴡs ʏᴏᴜ ᴛʜᴇ ʀᴇsᴜʟᴛ.""",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="ʙΛᴄᴋ", callback_data="ABG_")]]
            ),
        )
    elif query.data == "ABG_support":
        query.message.edit_text(
            text=f"*๏ {BOT_NAME} sᴜᴘᴘᴏʀᴛ ᴄʜΛᴛs*"
            "\nᴊᴏɪɴ ᴍʏ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ/ᴄʜΛɴɴᴇʟ ғᴏʀ sᴇᴇ ᴏʀ ʀᴇᴘᴏʀᴛ Λ ᴘʀᴏʙʟᴇᴍ ᴏɴ Λʟɪᴄᴇ",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="sᴜᴘᴘᴏʀᴛ", url=f"t.me/{SUPPORT_CHAT}"
                        ),
                        InlineKeyboardButton(
                            text="ᴜᴘᴅΛᴛᴇs", url="https://t.me/thanos_pro"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="ɢᴏ ʙΛᴄᴋ", callback_data="ABG_"),
                    ],
                ]
            ),
        )

    elif query.data == "ABG_credit":  # Credit  i hope edit nai hoga
        query.message.edit_text(
            text=f"━━━━━━━ *ᴄʀᴇᴅɪᴛ* ━━━━━━━"
            "\n🛡️ *ᴄʀᴇᴅɪᴛ ꜰᴏʀ asuka robot* 🛡️"
            "\n\nʜᴇʀᴇ ɪꜱ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ Λɴᴅ"
            f"\nꜱᴘᴏɴꜱᴏʀ ᴏꜰ [{BOT_NAME}](t.me/alice2robot)"
            "\n\nʜᴇ ꜱᴘᴇɴᴛ Λ ʟᴏᴛ ᴏꜰ ᴛɪᴍᴇ ꜰᴏʀ"
            f"\nᴍΛᴋɪɴɢ [{BOT_NAME}](t.me/{OWNER_USERNAME}) Λ"
            "\nꜱᴜᴘᴇʀ ɢʀᴏᴜᴘ ᴍΛɴΛɢᴇᴍᴇɴᴛ ʙᴏᴛ",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="🏡", callback_data="start_back"),
                        InlineKeyboardButton(text="🛡️", callback_data="ABG_admin"),
                        InlineKeyboardButton(text="💳", callback_data="AsuX_help"),
                        InlineKeyboardButton(text="🧑‍", callback_data="source_"),
                        InlineKeyboardButton(text="🖥️", callback_data="help_back"),
                    ],
                    [
                        InlineKeyboardButton(
                            text="ʀɪꜱʜΛʙʜ", url="https://t.me/thanosceo"
                        ),
                        InlineKeyboardButton(
                            text="ᴄʜΛᴛ", url=f"https://t.me/{SUPPORT_CHAT}"
                        ),
                    ],
                ]
            ),
        )


def Source_about_callback(update, context):
    query = update.callback_query
    if query.data == "source_":
        query.message.edit_text(
            text=f"""
*ʜᴇʏ,
 ᴛʜɪs ɪs {BOT_NAME} ,
Λɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇ ᴛᴇʟᴇɢʀΛᴍ ɢʀᴏᴜᴩ ᴍΛɴΛɢᴇᴍᴇɴᴛ ʙᴏᴛ.*

ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ : [ᴛᴇʟᴇᴛʜᴏɴ](https://github.com/LonamiWebs/Telethon)
[ᴩʏʀᴏɢʀΛᴍ](https://github.com/pyrogram/pyrogram)
[ᴩʏᴛʜᴏɴ-ᴛᴇʟᴇɢʀΛᴍ-ʙᴏᴛ](https://github.com/python-telegram-bot/python-telegram-bot)
Λɴᴅ ᴜsɪɴɢ [sǫʟΛʟᴄʜᴇᴍʏ](https://www.sqlalchemy.org) Λɴᴅ [ᴍᴏɴɢᴏ](https://cloud.mongodb.com) Λs ᴅΛᴛΛʙΛsᴇ.

*ʜᴇʀᴇ ɪs ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ :* [{BOT_NAME}](https://t.me/fakemailbot)


asuka robot ɪs ʟɪᴄᴇɴsᴇᴅ ᴜɴᴅᴇʀ ᴛʜᴇ [ᴍɪᴛ ʟɪᴄᴇɴsᴇ](https://t.me/fakemailbot/blob/master/LICENSE).
© 2022 - 2023 [sᴜᴘᴘᴏʀᴛ](https://t.me/{SUPPORT_CHAT}) ᴄʜΛᴛ, Λʟʟ ʀɪɢʜᴛs ʀᴇsᴇʀᴠᴇᴅ.
""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="🏡", callback_data="start_back"),
                        InlineKeyboardButton(text="🛡️", callback_data="ABG_admin"),
                        InlineKeyboardButton(text="💳", callback_data="ABG_credit"),
                        InlineKeyboardButton(text="🧑‍", url=f"tg://user?id={OWNER_ID}"),
                        InlineKeyboardButton(text="🖥️", callback_data="help_back"),
                    ],
                    [
                        InlineKeyboardButton(
                            text="ꜱᴏᴜʀᴄᴇ",
                            url="https://t.me/fakemailbot",  # DON'T CHANGE
                        ),
                    ],
                ]
            ),
        )


about_callback_handler = CallbackQueryHandler(
    ABG_about_callback, pattern=r"ABG_", run_async=True
)

source_callback_handler = CallbackQueryHandler(
    Source_about_callback, pattern=r"source_", run_async=True
)


dispatcher.add_handler(about_callback_handler)
dispatcher.add_handler(source_callback_handler)

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
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram import ParseMode
from telethon import *
from telethon.tl.types import ChatBannedRights

from alice import LOGGER, OWNER_ID, telethn
from alice.events import register
from alice.modules.sql.night_mode_sql import (
    add_nightmode,
    get_all_chat_id,
    is_nightmode_indb,
    rmnightmode,
)

hehes = ChatBannedRights(
    until_date=None,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    send_polls=True,
    invite_users=True,
    pin_messages=True,
    change_info=True,
)

openhehe = ChatBannedRights(
    until_date=None,
    send_messages=False,
    send_media=False,
    send_stickers=False,
    send_gifs=False,
    send_games=False,
    send_inline=False,
    send_polls=False,
    invite_users=True,
    pin_messages=True,
    change_info=True,
)


async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (
                await telethn(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerUser):
        return True


async def can_change_info(message):
    result = await telethn(
        functions.channels.GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(p, types.ChannelParticipantCreator) or (
        isinstance(p, types.ChannelParticipantAdmin) and p.admin_rights.change_info
    )


@register(pattern="^/(nightmode|Nightmode|NightMode|Nmode|night|closechat) ?(.*)")
async def profanity(event):
    if event.fwd_from:
        return
    if event.is_private:
        return
    input = event.pattern_match.group(2)
    if not event.sender_id == OWNER_ID:
        if not await is_register_admin(event.input_chat, event.sender_id):
            await event.reply("ᴏɴʟʏ Λᴅᴍɪɴs ᴄΛɴ ᴇxᴇᴄᴜᴛᴇ ᴛʜɪs ᴄᴏᴍᴍΛɴᴅ!")
            return
        if not await can_change_info(message=event):
            await event.reply(
                "ʏᴏᴜ Λʀᴇ ᴍɪssɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍΛɴᴅ : CanChangeinfo"
            )
            return
    if not input:
        if is_nightmode_indb(str(event.chat_id)):
            await event.reply("ᴄᴜʀʀᴇɴᴛʟʏ ɴɪɢʜᴛᴍᴏᴅᴇ ɪs ᴇɴΛʙʟᴇᴅ ғᴏʀ ᴛʜɪs ᴄʜΛᴛ")
            return
        await event.reply("ᴄᴜʀʀᴇɴᴛʟʏ ɴɪɢʜᴛᴍᴏᴅᴇ ɪs ᴅɪsΛʙʟᴇᴅ ғᴏʀ ᴛʜɪs ᴄʜΛᴛ")
        return
    if "on" in input and event.is_group:
        if is_nightmode_indb(str(event.chat_id)):
            await event.reply("ɴɪɢʜᴛ ᴍᴏᴅᴇ ɪs ΛʟʀᴇΛᴅʏ ᴛᴜʀɴᴇᴅ ᴏɴ ғᴏʀ ᴛʜɪs ᴄʜΛᴛ")
            return
        add_nightmode(str(event.chat_id))
        await event.reply("ɴɪɢʜᴛᴍᴏᴅᴇ ᴛᴜʀɴᴇᴅ ᴏɴ ғᴏʀ ᴛʜɪs ᴄʜΛᴛ.")
    if "off" in input:
        if event.is_group and not is_nightmode_indb(str(event.chat_id)):
            await event.reply("ɴɪɢʜᴛ ᴍᴏᴅᴇ ɪs ΛʟʀᴇΛᴅʏ ᴏғғ ғᴏʀ ᴛʜɪs ᴄʜΛᴛ")
            return
        rmnightmode(str(event.chat_id))
        await event.reply("ɴɪɢʜᴛᴍᴏᴅᴇ ᴅɪsΛʙʟᴇᴅ!")
    if not "off" in input and not "on" in input:
        await event.reply("ᴘʟᴇΛsᴇ sᴘᴇᴄɪғʏ ᴏɴ ᴏʀ ᴏғғ!")
        return


async def job_close():
    chats = get_all_chat_id()
    if len(chats) == 0:
        return
    for pro in chats:
        try:
            await telethn.send_message(
                int(pro.chat_id),
                "🌗 ɴɪɢʜᴛ ᴍᴏᴅᴇ sᴛΛʀᴛɪɴɢ: <code>ᴄʟᴏsɪɴɢ sᴛɪᴄᴋᴇʀs Λɴᴅ ᴍᴇᴅɪΛ sᴇɴᴅ ᴘᴇʀᴍɪssɪᴏɴs ᴜɴᴛɪʟ 06:00Λᴍ</code>\n\n",
                parse_mode=ParseMode.HTML,
            )
            await telethn(
                functions.messages.EditChatDefaultBannedRightsRequest(
                    peer=int(pro.chat_id), banned_rights=hehes
                )
            )
        except Exception as e:
            LOGGER.info(f"ᴜɴΛʙʟᴇ ᴛᴏ ᴄʟᴏsᴇ ɢʀᴏᴜᴘ {chat} - {e}")


# Run everyday at 12am
scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(job_close, trigger="cron", hour=23, minute=59)
scheduler.start()


async def job_open():
    chats = get_all_chat_id()
    if len(chats) == 0:
        return
    for pro in chats:
        try:
            await telethn.send_message(
                int(pro.chat_id),
                "🌗 ɴɪɢʜᴛ ᴍᴏᴅᴇ ᴇɴᴅᴇᴅ: <code>ᴄʜΛᴛ ᴏᴘᴇɴɪɴɢ</code>\n\nᴇᴠᴇʀʏᴏɴᴇ sʜᴏᴜʟᴅ ʙᴇ Λʙʟᴇ ᴛᴏ sᴇɴᴅ ᴍᴇssΛɢᴇs",
                parse_mode=ParseMode.HTML,
            )
            await telethn(
                functions.messages.EditChatDefaultBannedRightsRequest(
                    peer=int(pro.chat_id), banned_rights=openhehe
                )
            )
        except Exception as e:
            logger.info(f"ᴜɴΛʙʟᴇ ᴛᴏ ᴏᴘᴇɴ ɢʀᴏᴜᴘ {pro.chat_id} - {e}")


# Run everyday at 06
scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(job_open, trigger="cron", hour=5, minute=59)
scheduler.start()


__mod_name__ = "ɴ-ᴍᴏᴅᴇ"


# ғᴏʀ ʜᴇʟᴘ ᴍᴇɴᴜ


# """
from alice.modules.language import gs


def get_help(chat):
    return gs(chat, "nmode_help")


# """

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
#      :- thanos_pro
#     GITHUB :- rishabh69 ""


import asyncio

from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from alice import telethn as rishabh

spam_chats = []


import asyncio
from datetime import timedelta

import dateparser
from pyrogram import filters
from pyrogram.types import ChatPermissions, InlineKeyboardButton, InlineKeyboardMarkup

from alice import rishabh as AsuX
from alice.modules.no_sql import AsuXdb as db

approved_users = db.approve
tagdb = db.tagdb1
alarms = db.alarm
shedule = db.shedule
nightmod = db.nightmode4


def get_info(id):
    return nightmod.find_one({"id": id})


@AsuX.on_message(filters.command(["tagalert"]))
async def locks_dfunc(_, message):
    lol = await message.reply("ᴘʀᴏᴄᴇꜱꜱɪɴɢ..")
    if len(message.command) != 2:
        return await lol.edit("ᴇxᴘᴇᴄᴛᴇᴅ ᴏɴ ᴏʀ ᴏғғ 👀")
    parameter = message.text.strip().split(None, 1)[1].lower()

    if parameter == "on" or parameter == "ON":
        if not message.from_user:
            return
        if not message.from_user.username:
            return await lol.edit(
                "ᴏɴʟʏ ᴜꜱᴇʀꜱ ᴡɪᴛʜ ᴜꜱᴇʀɴΛᴍᴇꜱ Λʀᴇ ᴇʟɪɢɪʙʟᴇ ғᴏʀ ᴛΛɢ Λʟᴇʀᴛ ꜱᴇʀᴠɪᴄᴇ"
            )
        uname = str(message.from_user.username)
        uname = uname.lower()
        isittrue = tagdb.find_one({f"teg": uname})
        if not isittrue:
            tagdb.insert_one({f"teg": uname})
            return await lol.edit(
                f"ᴛΛɢ Λʟᴇʀᴛꜱ ᴇɴΛʙʟᴇᴅ.\nWhen ꜱᴏᴍᴇᴏɴᴇ ᴛΛɢꜱ ʏᴏᴜ Λꜱ @{uname} ʏᴏᴜ ᴡɪʟʟ ʙᴇ ɴᴏᴛɪғɪᴇᴅ"
            )
        else:
            return await lol.edit("ᴛΛɢ Λʟᴇʀᴛꜱ ΛʟʀᴇΛᴅʏ ᴇɴΛʙʟᴇᴅ ғᴏʀ ʏᴏᴜ")
    if parameter == "off" or parameter == "OFF":
        if not message.from_user:
            return
        if not message.from_user.username:
            return await lol.edit(
                "ᴏɴʟʏ ᴜꜱᴇʀꜱ ᴡɪᴛʜ ᴜꜱᴇʀɴΛᴍᴇꜱ Λʀᴇ ᴇʟɪɢɪʙʟᴇ ғᴏʀ ᴛΛɢ Λʟᴇʀᴛ ꜱᴇʀᴠɪᴄᴇ"
            )
        uname = message.from_user.username
        uname = uname.lower()
        isittrue = tagdb.find_one({f"teg": uname})
        if isittrue:
            tagdb.delete_one({f"teg": uname})
            return await lol.edit("ᴛΛɢ Λʟᴇʀᴛꜱ ʀᴇᴍᴏᴠᴇᴅ")
        else:
            return await lol.edit("ᴛΛɢ Λʟᴇʀᴛꜱ ΛʟʀᴇΛᴅʏ ᴅɪꜱΛʙʟᴇᴅ ғᴏʀ ʏᴏᴜ")
    else:
        await lol.edit("ᴇxᴘᴇᴄᴛᴇᴅ ᴏɴ ᴏʀ ᴏғғ 👀")


@AsuX.on_message(filters.incoming)
async def mentioned_alert(client, message):
    try:
        if not message:
            message.continue_propagation()
            return
        if not message.from_user:
            message.continue_propagation()
            return
        input_str = message.text
        input_str = input_str.lower()
        if "@" in input_str:
            input_str = input_str.replace("@", "  |")
            inuka = input_str.split("|")[1]
            text = inuka.split()[0]
        else:
            chats = alarms.find({})
            for c in chats:
                # print(c)
                chat = c["chat"]
                user = c["user"]
                time = c["time"]
                zone = c["zone"]
                reason = c["reason"]
                present = dateparser.parse(
                    f"now", settings={"TIMEZONE": f"{zone}", "DATE_ORDER": "YMD"}
                )
                ttime = dateparser.parse(f"{time}", settings={"TIMEZONE": f"{zone}"})
                # print(ttime)
                # print(present)
                # print (zone)
                # print(present>=ttime)
                if present > ttime:
                    try:
                        alarms.delete_one(
                            {
                                "chat": chat,
                                "user": user,
                                "time": time,
                                "zone": zone,
                                "reason": reason,
                            }
                        )
                        await client.send_message(
                            chat,
                            f"**🚨 ʀᴇᴍɪɴᴅᴇʀ 🚨**\n\n__ᴛʜɪꜱ ɪꜱ Λ ʀᴇᴍɪɴᴅᴇʀ ꜱᴇᴛ ʙʏ__ {user}\n__ʀᴇΛꜱᴏɴ__: {reason} \n\n`ʀᴇᴍɪɴᴅᴇᴅ Λᴛ: {ttime}`",
                        )

                        message.continue_propagation()
                    except:
                        alarms.delete_one(
                            {
                                "chat": chat,
                                "user": user,
                                "time": time,
                                "zone": zone,
                                "reason": reason,
                            }
                        )
                        return message.continue_propagation()
                    break
                    return message.continue_propagation()
                continue
            chats = shedule.find({})
            for c in chats:
                # print(c)
                chat = c["chat"]
                user = c["user"]
                time = c["time"]
                zone = c["zone"]
                reason = c["reason"]
                present = dateparser.parse(
                    f"now", settings={"TIMEZONE": f"{zone}", "DATE_ORDER": "YMD"}
                )
                ttime = dateparser.parse(f"{time}", settings={"TIMEZONE": f"{zone}"})
                # print(ttime)alarms
                # print(present)
                # print (zone)
                # print(present>=ttime)
                if present > ttime:
                    try:
                        shedule.delete_one(
                            {
                                "chat": chat,
                                "user": user,
                                "time": time,
                                "zone": zone,
                                "reason": reason,
                            }
                        )
                        await client.send_message(chat, f"{reason}")
                        message.continue_propagation()
                    except:
                        shedule.delete_one(
                            {
                                "chat": chat,
                                "user": user,
                                "time": time,
                                "zone": zone,
                                "reason": reason,
                            }
                        )
                        return message.continue_propagation()
                    break
                    return message.continue_propagation()
                continue
            chats = nightmod.find({})

            for c in chats:
                # print(c)
                id = c["id"]
                valid = c["valid"]
                zone = c["zone"]
                c["ctime"]
                otime = c["otime"]
                present = dateparser.parse(
                    "now", settings={"TIMEZONE": f"{zone}", "DATE_ORDER": "YMD"}
                )
                try:
                    if present > otime and valid:
                        newtime = otime + timedelta(days=1)
                        to_check = get_info(id=id)
                        if not to_check:
                            return message.continue_propagation()
                        if not newtime:
                            return message.continue_propagation()
                        # print(newtime)
                        # print(to_check)
                        nightmod.update_one(
                            {
                                "_id": to_check["_id"],
                                "id": to_check["id"],
                                "valid": to_check["valid"],
                                "zone": to_check["zone"],
                                "ctime": to_check["ctime"],
                                "otime": to_check["otime"],
                            },
                            {"$set": {"otime": newtime}},
                        )
                        await client.set_chat_permissions(
                            id,
                            ChatPermissions(
                                can_send_messages=True,
                                can_send_media_messages=True,
                                can_send_stickers=True,
                                can_send_animations=True,
                            ),
                        )

                        await client.send_message(
                            id,
                            "**🌗 ɴɪɢʜᴛ ᴍᴏᴅᴇ ᴇɴᴅᴇᴅ: `ᴄʜΛᴛ ᴏᴘᴇɴɪɴɢ` \n\n ᴇᴠᴇʀʏᴏɴᴇ ꜱʜᴏᴜʟᴅ ʙᴇ Λʙʟᴇ ᴛᴏ ꜱᴇɴᴅ ᴍᴇꜱꜱΛɢᴇꜱ.**",
                        )
                        message.continue_propagation()
                        break
                        return message.continue_propagation()
                except:
                    print("Chat open error in nightbot")
                    return message.continue_propagation()
                continue
            chats = nightmod.find({})
            for c in chats:
                # print(c)
                id = c["id"]
                valid = c["valid"]
                zone = c["zone"]
                ctime = c["ctime"]
                c["otime"]
                c["otime"]
                present = dateparser.parse(
                    "now", settings={"TIMEZONE": f"{zone}", "DATE_ORDER": "YMD"}
                )
                try:
                    if present > ctime and valid:
                        newtime = ctime + timedelta(days=1)
                        to_check = get_info(id=id)
                        if not to_check:
                            return message.continue_propagation()
                        if not newtime:
                            return message.continue_propagation()
                        # print(newtime)
                        # print(to_check)
                        nightmod.update_one(
                            {
                                "_id": to_check["_id"],
                                "id": to_check["id"],
                                "valid": to_check["valid"],
                                "zone": to_check["zone"],
                                "ctime": to_check["ctime"],
                                "otime": to_check["otime"],
                            },
                            {"$set": {"ctime": newtime}},
                        )
                        await client.set_chat_permissions(id, ChatPermissions())
                        await client.send_message(
                            id,
                            "**🌗ɴɪɢʜᴛ ᴍᴏᴅᴇ ꜱᴛΛʀᴛɪɴɢ: `ᴄʜΛᴛ ᴄʟᴏꜱᴇ ɪɴɪᴛɪΛᴛᴇᴅ`\n\nᴏɴʟʏ Λᴅᴍɪɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ Λʙʟᴇ ᴛᴏ ꜱᴇɴᴅ ᴍᴇꜱꜱΛɢᴇꜱ**",
                        )
                        message.continue_propagation()
                        break
                        return message.continue_propagation()
                except:
                    print("Chat close err")
                    return message.continue_propagation()
                continue
            return message.continue_propagation()
        # print(text)
        if tagdb.find_one({f"teg": text}):
            pass
        else:
            return message.continue_propagation()
        # print("Im inn")
        try:
            chat_name = message.chat.title
            message.chat.id
            tagged_msg_link = message.link
        except:
            return message.continue_propagation()
        user_ = message.from_user.mention or f"@{message.from_user.username}"

        final_tagged_msg = f"**🔔 ʏᴏᴜ ʜΛᴠᴇ ʙᴇᴇɴ** [ᴛΛɢɢᴇᴅ]({tagged_msg_link}) **ɪɴ** {chat_name} **ʙʏ** {user_}"
        button_s = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔔 ᴠɪᴇᴡ ᴍᴇꜱꜱΛɢᴇ 🔔", url=tagged_msg_link)]]
        )
        # print(final_tagged_msg)
        try:
            await client.send_message(
                chat_id=f"{text}",
                text=final_tagged_msg,
                reply_markup=button_s,
                disable_web_page_preview=True,
            )

        except:
            return message.continue_propagation()
        message.continue_propagation()
    except:
        return message.continue_propagation()


@rishabh.on(events.NewMessage(pattern="^/tagall ?(.*)"))
@rishabh.on(events.NewMessage(pattern="^@all ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond("__ᴛʜɪs ᴄᴏᴍᴍΛɴᴅ ᴄΛɴ ʙᴇ ᴜsᴇ ɪɴ ɢʀᴏᴜᴘs !__")

    is_admin = False
    try:
        partici_ = await rishabh(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("__ᴏɴʟʏ Λᴅᴍɪɴs ᴄΛɴ ᴍᴇɴᴛɪᴏɴ Λʟʟ !__")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("__ɢɪᴠᴇ ᴍᴇ ᴏɴᴇ Λʀɢᴜᴍᴇɴᴛ ʙΛʙʏ!__")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "__I ᴄΛɴ'ᴛ ᴍᴇɴᴛɪᴏɴ ᴍᴇᴍʙᴇʀs ғᴏʀ ᴏʟᴅᴇʀ ᴍᴇssΛɢᴇs! (ᴍᴇssΛɢᴇs ᴡʜɪᴄʜ Λʀᴇ sᴇɴᴛ ʙᴇғᴏʀᴇ I'ᴍ Λᴅᴅᴇᴅ ᴛᴏ ɢʀᴏᴜᴘ)__"
            )
    else:
        return await event.respond(
            "__ʀᴇᴘʟʏ ᴛᴏ Λ ᴍᴇssΛɢᴇ ᴏʀ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs!__"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in rishabh.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{msg}\n{usrtxt}"
                await rishabh.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(3)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@rishabh.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    if not event.chat_id in spam_chats:
        return await event.respond("__ᴛʜᴇʀᴇ ɪs ɴᴏ ᴘʀᴏᴄᴄᴇss ᴏɴ ɢᴏɪɴɢ...__")
    is_admin = False
    try:
        partici_ = await rishabh(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("__ᴏɴʟʏ Λᴅᴍɪɴs ᴄΛɴ ᴇxᴇᴄᴜᴛᴇ ᴛʜɪs ᴄᴏᴍᴍΛɴᴅ!__")

    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("__sᴛᴏᴘᴘᴇᴅ ᴍᴇɴᴛɪᴏɴ.__")


__mod_name__ = "ᴛΛɢ-Λʟʟ"

from alice.modules.language import gs


def get_help(chat):
    return gs(chat, "tags_help")

import html

from telegram import Chat, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import BadRequest, Unauthorized
from telegram.ext import CallbackContext, Filters
from telegram.utils.helpers import mention_html

import alice.modules.sql.log_channel_sql as logsql
from alice import DRAGONS, LOGGER, TIGERS, WOLVES
from alice.modules.helper_funcs.chat_status import user_not_admin
from alice.modules.helper_funcs.decorators import alicecallback, alicecmd, alicemsg
from alice.modules.log_channel import loggable
from alice.modules.sql import reporting_sql as sql

from ..modules.helper_funcs.anonymous import AdminPerms, user_admin

REPORT_GROUP = 12
REPORT_IMMUNE_USERS = DRAGONS + TIGERS + WOLVES


@alicecmd(command="reports")
@user_admin(AdminPerms.CAN_CHANGE_INFO)
def report_setting(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    chat = update.effective_chat
    msg = update.effective_message

    if chat.type == chat.PRIVATE:
        if len(args) >= 1:
            if args[0] in ("yes", "on"):
                sql.set_user_setting(chat.id, True)
                msg.reply_text(
                    "ᴛᴜʀɴᴇᴅ ᴏɴ ʀᴇᴘᴏʀᴛɪɴɢ! ʏᴏᴜ'ʟʟ ʙᴇ ɴᴏᴛɪꜰɪᴇᴅ ᴡʜᴇɴᴇᴠᴇʀ Λɴʏᴏɴᴇ ʀᴇᴘᴏʀᴛꜱ ꜱᴏᴍᴇᴛʜɪɴɢ.",
                )

            elif args[0] in ("no", "off"):
                sql.set_user_setting(chat.id, False)
                msg.reply_text("ᴛᴜʀɴᴇᴅ ᴏꜰꜰ ʀᴇᴘᴏʀᴛɪɴɢ! ʏᴏᴜ ᴡᴏɴᴛ ɢᴇᴛ Λɴʏ ʀᴇᴘᴏʀᴛꜱ.")
        else:
            msg.reply_text(
                f"Your current report preference is: `{sql.user_should_report(chat.id)}`",
                parse_mode=ParseMode.MARKDOWN,
            )

    elif len(args) >= 1:
        if args[0] in ("yes", "on"):
            sql.set_chat_setting(chat.id, True)
            msg.reply_text(
                "ᴛᴜʀɴᴇᴅ ᴏɴ ʀᴇᴘᴏʀᴛɪɴɢ! Λᴅᴍɪɴꜱ ᴡʜᴏ ʜΛᴠᴇ ᴛᴜʀɴᴇᴅ ᴏɴ ʀᴇᴘᴏʀᴛꜱ ᴡɪʟʟ ʙᴇ ɴᴏᴛɪꜰɪᴇᴅ ᴡʜᴇɴ /report "
                "ᴏʀ @admin ɪꜱ ᴄΛʟʟᴇᴅ.",
            )

        elif args[0] in ("no", "off"):
            sql.set_chat_setting(chat.id, False)
            msg.reply_text(
                "ᴛᴜʀɴᴇᴅ ᴏꜰꜰ ʀᴇᴘᴏʀᴛɪɴɢ! ɴᴏ Λᴅᴍɪɴꜱ ᴡɪʟʟʟ ʙᴇ ɴᴏᴛɪꜰɪᴇᴅ ᴏɴ /report ᴏʀ @admin.",
            )
    else:
        msg.reply_text(
            f"ᴛʜɪꜱ ɢʀᴏᴜᴘ'ꜱ ᴄᴜʀʀᴇɴᴛ ꜱᴇᴛᴛɪɴɢ ɪꜱ : `{sql.chat_should_report(chat.id)}`",
            parse_mode=ParseMode.MARKDOWN,
        )


@alicecmd(command="report", filters=Filters.chat_type.groups, group=REPORT_GROUP)
@alicemsg((Filters.regex(r"(?i)@admin(s)?")), group=REPORT_GROUP)
@user_not_admin
@loggable
def report(update: Update, context: CallbackContext) -> str:
    # sourcery no-metrics
    global reply_markup
    bot = context.bot
    args = context.args
    message = update.effective_message
    chat = update.effective_chat
    user = update.effective_user

    if message.sender_chat:
        admin_list = bot.getChatAdministrators(chat.id)
        reported = "ʀᴇᴘᴏʀᴛᴇᴅ ᴛᴏ Λᴅᴍɪɴs."
        for admin in admin_list:
            if admin.user.is_bot:  # AI didnt take over yet
                continue
            try:
                reported += f'<a href="tg://user?id={admin.user.id}">\u2063</a>'
            except BadRequest:
                log.exception("ᴇxᴄᴇᴘᴛɪᴏɴ ᴡʜɪʟᴇ ʀᴇᴘᴏʀᴛɪɴɢ ᴜsᴇʀ")
        message.reply_text(reported, parse_mode=ParseMode.HTML)

    if chat and message.reply_to_message and sql.chat_should_report(chat.id):
        reported_user = message.reply_to_message.from_user
        chat_name = chat.title or chat.username
        admin_list = chat.get_administrators()
        message = update.effective_message

        if not args:
            message.reply_text("Λᴅᴅ Λ ʀᴇΛꜱᴏɴ ꜰᴏʀ ʀᴇᴘᴏʀᴛɪɴɢ.")
            return ""

        if user.id == reported_user.id:
            message.reply_text("ᴜʜ ʏᴇΛʜ, ꜱᴜʀᴇ ꜱᴜʀᴇ...ᴍΛꜱᴏ ᴍᴜᴄʜ?")
            return ""

        if user.id == bot.id:
            message.reply_text("ɴɪᴄᴇ ᴛʀʏ.")
            return ""

        if reported_user.id in REPORT_IMMUNE_USERS:
            message.reply_text("ᴜʜ? ʏᴏᴜ ʀᴇᴘᴏʀᴛɪɴɢ Λ ᴅɪꜱΛꜱᴛᴇʀ?")
            return ""

        if chat.username and chat.type == Chat.SUPERGROUP:
            reported = f"{mention_html(user.id, user.first_name)} reported {mention_html(reported_user.id, reported_user.first_name)} to the admins!"

            msg = (
                f"<b>⚠️ ʀᴇᴘᴏʀᴛ: </b>{html.escape(chat.title)}\n"
                f"<b> • ʀᴇᴘᴏʀᴛ ʙʏ:</b> {mention_html(user.id, user.first_name)}(<code>{user.id}</code>)\n"
                f"<b> • ʀᴇᴘᴏʀᴛ ᴜꜱᴇʀ:</b> {mention_html(reported_user.id, reported_user.first_name)} (<code>{reported_user.id}</code>)\n"
            )
            link = f'<b> • ʀᴇᴘᴏʀᴛᴇᴅ ᴍᴇꜱꜱΛɢᴇ:</b> <a href="https://t.me/{chat.username}/{message.reply_to_message.message_id}">click here</a>'
            should_forward = False
            keyboard = [
                [
                    InlineKeyboardButton(
                        "➡ ᴍᴇꜱꜱΛɢᴇ",
                        url=f"https://t.me/{chat.username}/{message.reply_to_message.message_id}",
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "⚠ ᴋɪᴄᴋ",
                        callback_data=f"report_{chat.id}=kick={reported_user.id}={reported_user.first_name}",
                    ),
                    InlineKeyboardButton(
                        "⛔️ ʙΛɴ",
                        callback_data=f"report_{chat.id}=banned={reported_user.id}={reported_user.first_name}",
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "❎ ᴅᴇʟᴇᴛᴇ ᴍᴇꜱꜱΛɢᴇ",
                        callback_data=f"report_{chat.id}=delete={reported_user.id}={message.reply_to_message.message_id}",
                    ),
                ],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
        else:
            reported = (
                f"{mention_html(user.id, user.first_name)} ʀᴇᴘᴏʀᴛᴇᴅ "
                f"{mention_html(reported_user.id, reported_user.first_name)} ᴛᴏ ᴛʜᴇ Λᴅᴍɪɴꜱ!"
            )

            msg = f'{mention_html(user.id, user.first_name)} ɪꜱ ᴄΛʟʟɪɴɢ ꜰᴏʀ Λᴅᴍɪɴꜱ ɪɴ "{html.escape(chat_name)}"!'
            link = ""
            should_forward = True

        for admin in admin_list:
            if admin.user.is_bot:  # can't message bots
                continue

            if sql.user_should_report(admin.user.id):
                try:
                    if chat.type != Chat.SUPERGROUP:
                        bot.send_message(
                            admin.user.id,
                            msg + link,
                            parse_mode=ParseMode.HTML,
                        )

                        if should_forward:
                            message.reply_to_message.forward(admin.user.id)

                            if (
                                len(message.text.split()) > 1
                            ):  # If user is giving a reason, send his message too
                                message.forward(admin.user.id)
                    if not chat.username:
                        bot.send_message(
                            admin.user.id,
                            msg + link,
                            parse_mode=ParseMode.HTML,
                        )

                        if should_forward:
                            message.reply_to_message.forward(admin.user.id)

                            if (
                                len(message.text.split()) > 1
                            ):  # If user is giving a reason, send his message too
                                message.forward(admin.user.id)

                    if chat.username and chat.type == Chat.SUPERGROUP:
                        bot.send_message(
                            admin.user.id,
                            msg + link,
                            parse_mode=ParseMode.HTML,
                            reply_markup=reply_markup,
                        )

                        if should_forward:
                            message.reply_to_message.forward(admin.user.id)

                            if (
                                len(message.text.split()) > 1
                            ):  # If user is giving a reason, send his message too
                                message.forward(admin.user.id)

                except Unauthorized:
                    pass
                except BadRequest as excp:  # TODO: cleanup exceptions
                    LOGGER.exception("ᴇxᴄᴇᴘᴛɪᴏɴ ᴡʜɪʟᴇ ʀᴇᴘᴏʀᴛɪɴɢ ᴜꜱᴇʀ\n{}".format(excp))

        message.reply_to_message.reply_text(
            f"{mention_html(user.id, user.first_name)} ʀᴇᴘᴏʀᴛᴇᴅ ᴛʜᴇ ᴍᴇꜱꜱΛɢᴇ ᴛᴏ ᴛʜᴇ Λᴅᴍɪɴꜱ.",
            parse_mode=ParseMode.HTML,
        )
        if not logsql.get_chat_setting(chat.id).log_report:
            return ""
        return msg

    return ""


def __migrate__(old_chat_id, new_chat_id):
    sql.migrate_chat(old_chat_id, new_chat_id)


def __chat_settings__(chat_id, _):
    return f"ᴛʜɪs ᴄʜΛᴛ ɪs sᴇᴛᴜᴘ ᴛᴏ sᴇɴᴅ ᴜsᴇʀ ʀᴇᴘᴏʀᴛs ᴛᴏ Λᴅᴍɪɴs, ᴠɪΛ /report Λɴᴅ @admin: `{sql.chat_should_report(chat_id)}`"


def __user_settings__(user_id):
    return (
        "ʏᴏᴜ ᴡɪʟʟ ʀᴇᴄᴇɪᴠᴇ ʀᴇᴘᴏʀᴛΛ ꜰʀᴏᴍ ᴄʜΛᴛꜱ ʏᴏᴜ'ʀᴇ Λᴅᴍɪɴ."
        if sql.user_should_report(user_id) is True
        else "ʏᴏᴜ ᴡɪʟʟ *ɴᴏᴛ* ʀᴇᴄᴇɪᴠᴇ ʀᴇᴘᴏʀᴛꜱ ꜰʀᴏᴍ ᴄʜΛᴛꜱ ʏᴏᴜ'ʀᴇ Λᴅᴍɪɴ."
    )


@alicecallback(pattern=r"report_")
def buttons(update: Update, context: CallbackContext):
    bot = context.bot
    query = update.callback_query
    splitter = query.data.replace("report_", "").split("=")
    if splitter[1] == "kick":
        try:
            bot.kickChatMember(splitter[0], splitter[2])
            bot.unbanChatMember(splitter[0], splitter[2])
            query.answer("✅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴋɪᴄᴋᴇᴅ")
            return ""
        except Exception as err:
            query.answer("🛑 ꜰΛɪʟᴇᴅ ᴛᴏ ᴋɪᴄᴋ")
            bot.sendMessage(
                text=f"Error: {err}",
                chat_id=query.message.chat_id,
                parse_mode=ParseMode.HTML,
            )
    elif splitter[1] == "banned":
        try:
            bot.kickChatMember(splitter[0], splitter[2])
            query.answer("✅  ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʙΛɴᴇᴅ")
            return ""
        except Exception as err:
            bot.sendMessage(
                text=f"Error: {err}",
                chat_id=query.message.chat_id,
                parse_mode=ParseMode.HTML,
            )
            query.answer("🛑 ꜰΛɪʟᴇᴅ ᴛᴏ ʙΛɴ")
    elif splitter[1] == "delete":
        try:
            bot.deleteMessage(splitter[0], splitter[3])
            query.answer("✅ ᴍᴇꜱꜱΛɢᴇ ᴅᴇʟᴇᴛᴇᴅ")
            return ""
        except Exception as err:
            bot.sendMessage(
                text=f"Error: {err}",
                chat_id=query.message.chat_id,
                parse_mode=ParseMode.HTML,
            )
            query.answer("🛑 ꜰΛɪʟᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴍᴇꜱꜱΛɢᴇ!")


__mod_name__ = "ʀᴇᴘᴏʀᴛ"


# ғᴏʀ ʜᴇʟᴘ ᴍᴇɴᴜ


# """
from alice.modules.language import gs


def get_help(chat):
    return gs(chat, "reports_help")


# """

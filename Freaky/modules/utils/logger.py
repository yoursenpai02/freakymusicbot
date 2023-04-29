from Freaky import bot
from Freaky.modules.database import is_on_off
from Freaky.utilities.config import LOG, LOG_GROUP_ID


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Chat"
        if message.from_user.username:
            user_name = f"@{message.from_user.username}"
        else:
            user_name = f"{message.from_user.mention}"
        logger_text = f"""
━━━━━━━━━━━━━━━━━━━
                    ᴄʜᴧᴍᴘᴜ
━━━━━━━━━━━━━━━━━━━
👻 ᴛᴇʟᴇɢʀᴀᴍ ᴜsᴇʀ ᴅᴇᴛᴀɪʟs  :
❄️ ɴᴀᴍᴇ › {message.from_user.first_name}
🌸 ʟɪɴᴋ : › {user_name}
🎀 ɪᴅ : › {message.from_user.id}
━━━━━━━━━━━━━━━━━━━
💕 ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀᴛ ᴅᴇᴛᴀɪʟs  :
❄️ ɴᴀᴍᴇ › {message.chat.title}
✨️ ʟɪɴᴋ : › {chatusername}
📝 ɪᴅ : › {message.chat.id}
━━━━━━━━━━━━━━━━━━━
                   [ ᴄʜᴧᴍᴘᴜ ](https://t.me/ll_Champu_ll).
━━━━━━━━━━━━━━━━━━━"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await bot.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return

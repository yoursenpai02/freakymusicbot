from typing import Union
from pyrogram.types import InlineKeyboardButton

from Freaky import bot
from Freaky.utilities.config import SUPPORT_CHANNEL, SUPPORT_GROUP


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❄️ᴄᴏᴍᴍᴀɴᴅs✨",
                url=f"https://t.me/{bot.username}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="🙄ᴜᴘᴅᴀᴛᴇs🤭",
                url=f"{SUPPORT_CHANNEL}",
            ),
            InlineKeyboardButton(
                text="🥺sᴜᴘᴘᴏʀᴛ😖",
                url=f"{SUPPORT_GROUP}",
            )
        ],
        [
            InlineKeyboardButton(
                text="🤖ʙᴏᴛ sᴇᴛᴛɪɴɢs ⚙️", callback_data="settings_helper"
            )
        ]
    ]
    return buttons

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="💋ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ🍑",
                url=f"https://t.me/{bot.username}?startgroup=true"),
        ],
        [
            InlineKeyboardButton(
                text="🙄ᴜᴘᴅᴀᴛᴇs🤭",
                url=f"{SUPPORT_CHANNEL}"),
            InlineKeyboardButton(
                text="🥺sᴜᴘᴘᴏʀᴛ😖",
                url=f"{SUPPORT_GROUP}")
        ],
        [
            InlineKeyboardButton(
                text="💕ᴄᴏᴍᴍᴀɴᴅ✨️",
                callback_data="settings_back_helper"
            )
        ]
    ]
    return buttons

def private_panelx(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="💋ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ🍑",
                url=f"https://t.me/{bot.username}?startgroup=true"),
        ],
        [
            InlineKeyboardButton(
                text="✨️ᴏᴘᴇɴ ᴄᴏᴍᴍᴀɴᴅ ᴍᴇɴᴜ🎀",
                callback_data="settings_back_helper"
            )
        ]
    ]
    return buttons

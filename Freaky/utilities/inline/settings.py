# Powered By @Freaky

from typing import Union

from pyrogram.types import InlineKeyboardButton


def setting_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔊ᴀᴜᴅɪᴏ ǫᴜᴀʟɪᴛʏ ", callback_data="AQ"
            ),
            InlineKeyboardButton(
                text="🎥ᴠɪᴅᴇᴏ ǫᴜᴀʟɪᴛʏ", callback_data="VQ"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🎩ᴀᴜᴛʜ ᴜsᴇʀs", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="ғʀᴇᴧᴋʏ", url=f"https://t.me/Freaky"
            ),
        ],
        [
            InlineKeyboardButton(
                text="▶️ᴘʟᴀʏ ᴍᴏᴅᴇ", callback_data="PM"
            ),
            InlineKeyboardButton(
                text="😕ᴄʟᴇᴀɴ ᴍᴏᴅᴇ", callback_data="CM"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❌ ᴄʟᴏsᴇ sᴇᴛᴛɪɴɢs  ❌", callback_data="close"
            ),
        ],
    ]
    return buttons


def audio_quality_markup(
    _,
    low: Union[bool, str] = None,
    medium: Union[bool, str] = None,
    high: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="{0} ʟᴏᴡ ǫᴜᴀʟɪᴛʏ ᴀᴜᴅɪᴏ".format("✅")
                if low == True
                else "{0} ʟᴏᴡ ǫᴜᴀʟɪᴛʏ ᴀᴜᴅɪᴏ".format(""),
                callback_data="LQA",
            )
        ],
        [
            InlineKeyboardButton(
                text="{0} ᴍᴇᴅɪᴜᴍ ǫᴜᴀʟɪᴛʏ ᴀᴜᴅɪᴏ ".format("✅")
                if medium == True
                else "{0} ᴍᴇᴅɪᴜᴍ ǫᴜᴀʟɪᴛʏ ᴀᴜᴅɪᴏ ".format(""),
                callback_data="MQA",
            )
        ],
        [
            InlineKeyboardButton(
                text="{0} ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴀᴜᴅɪᴏ ".format("✅")
                if high == True
                else "{0} ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴀᴜᴅɪᴏ ".format(""),
                callback_data="HQA",
            )
        ],
        [
            InlineKeyboardButton(
                text="⬅️ʙᴀᴄᴋ",
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text="❌ᴄʟᴏsᴇ", callback_data="close"
            ),
        ],
    ]
    return buttons


def video_quality_markup(
    _,
    low: Union[bool, str] = None,
    medium: Union[bool, str] = None,
    high: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="{0} ʟᴏᴡ ǫᴜᴀʟɪᴛʏ ᴠɪᴅᴇᴏ".format("✅")
                if low == True
                else "{0} ʟᴏᴡ ǫᴜᴀʟɪᴛʏ ᴠɪᴅᴇᴏ".format(""),
                callback_data="LQV",
            )
        ],
        [
            InlineKeyboardButton(
                text="{0} ᴍᴇᴅɪᴜᴍ ǫᴜᴀʟɪᴛʏ ᴠɪᴅᴇᴏ".format("✅")
                if medium == True
                else "{0} ᴍᴇᴅɪᴜᴍ ǫᴜᴀʟɪᴛʏ ᴠɪᴅᴇᴏ".format(""),
                callback_data="MQV",
            )
        ],
        [
            InlineKeyboardButton(
                text="{0} ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴠɪᴅᴇᴏ".format("✅")
                if high == True
                else "{0} ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴠɪᴅᴇᴏ".format(""),
                callback_data="HQV",
            )
        ],
        [
            InlineKeyboardButton(
                text="⬅️ʙᴀᴄᴋ",
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text="❌ᴄʟᴏsᴇ", callback_data="close"
            ),
        ],
    ]
    return buttons


def cleanmode_settings_markup(
    _,
    status: Union[bool, str] = None,
    dels: Union[bool, str] = None,
    sug: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔥ᴄʟᴇᴀɴ ᴍᴏᴅᴇ", callback_data="CMANSWER"
            ),
            InlineKeyboardButton(
                text="✅ᴇɴᴀʙʟᴇᴅ" if status == True else "❌ᴅɪsᴀʙʟᴇᴅ",
                callback_data="CLEANMODE",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🗑ᴄᴍᴅ ᴄʟᴇᴀɴ", callback_data="COMMANDANSWER"
            ),
            InlineKeyboardButton(
                text="✅ᴇɴᴀʙʟᴇᴅ" if dels == True else "❌ᴅɪsᴀʙʟᴇᴅ",
                callback_data="COMMANDELMODE",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🧑‍🚀sᴜɢɢ ᴍᴏᴅᴇ", callback_data="SUGGANSWER"
            ),
            InlineKeyboardButton(
                text="✅ᴇɴᴀʙʟᴇᴅ" if sug == True else "❌ᴅɪsᴀʙʟᴇᴅ",
                callback_data="SUGGESTIONCHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ʙᴀᴄᴋ",
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text="❌ᴄʟᴏsᴇ𝐞", callback_data="close"
            ),
        ],
    ]
    return buttons


def auth_users_markup(_, status: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎩ᴀᴜᴛʜ ᴜsᴇʀs", callback_data="AUTHANSWER"
            ),
            InlineKeyboardButton(
                text="👤ᴀᴅᴍɪɴs" if status == True else " 👥ᴇᴠᴇʀʏᴏɴᴇ",
                callback_data="AUTH",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📋ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛ", callback_data="AUTHLIST"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁ ʙᴀᴄᴋ",
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text="🇽 ᴄʟᴏsᴇ", callback_data="close"
            ),
        ],
    ]
    return buttons


def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔎sᴇᴀʀᴄʜ ᴍᴏᴅᴇ", callback_data="SEARCHANSWER"
            ),
            InlineKeyboardButton(
                text="✅ᴅɪʀᴇᴄᴛ" if Direct == True else "✅ɪɴʟɪɴᴇ",
                callback_data="MODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text="👨‍⚖️ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs", callback_data="AUTHANSWER"
            ),
            InlineKeyboardButton(
                text="👤ᴀᴅᴍɪɴs" if Group == True else "👥ᴇᴠᴇʀʏᴏɴᴇ",
                callback_data="CHANNELMODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🫂ᴘʟᴀʏ ᴛʏᴘᴇ", callback_data="PLAYTYPEANSWER"
            ),
            InlineKeyboardButton(
                text="👤ᴀᴅᴍɪɴs"
                if Playtype == True
                else "👥ᴇᴠᴇʀʏᴏɴᴇ" ,
                callback_data="PLAYTYPECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ʙᴀᴄᴋ",
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text="❌ᴄʟᴏsᴇ", callback_data="close"
            ),
        ],
    ]
    return buttons

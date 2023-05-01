import random
from pyrogram.types import InlineKeyboardButton

from Freaky.utilities.config import SUPPORT_GROUP


def stream_markup_timer(_, videoid, chat_id, played, dur):
    buttons = [
        [
            InlineKeyboardButton(
                                    "● 𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠 𝐂𝐥𝐮𝐛 ●", url=f"{SUPPORT_GROUP}"
                        ),
            InlineKeyboardButton(
                                    "●  ᴄʜᴧᴍᴘᴜ ●", url=f"https//t.me/TheShivanshu"
                        )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    buttons = [
        [
            InlineKeyboardButton(
                                                "● 𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠 𝐂𝐥𝐮𝐛 ●", url=f"{SUPPORT_GROUP}"
                                    ),
            InlineKeyboardButton(
                                    "●  ᴄʜᴧᴍᴘᴜ ●", url=f"https//t.me/TheShivanshu"
                        )
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                                                "● 𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠 𝐂𝐥𝐮𝐛 ●", url=f"{SUPPORT_GROUP}"
                                    ),
            InlineKeyboardButton(
                                    "●  ᴄʜᴧᴍᴘᴜ ●", url=f"https//t.me/TheShivanshu"
                        )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                                                "● 𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠 𝐂𝐥𝐮𝐛 ●", url=f"{SUPPORT_GROUP}"
                                    ),
            InlineKeyboardButton(
                                    "●  ᴄʜᴧᴍᴘᴜ ●", url=f"https//t.me/TheShivanshu"
                      )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔊ᴘʟᴀʏ ᴀᴜᴅɪᴏ",
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="📽️ᴘʟᴀʏ ᴠɪᴅᴇᴏ",
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🇽 ᴄʟᴏsᴇ 🇽",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔊ᴘʟᴀʏ ᴀᴜᴅɪᴏ",
                callback_data=f"ChampuPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="️📽️ᴘʟᴀʏ ᴠɪᴅᴇᴏ",
                callback_data=f"ChampuPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🇽 ᴄʟᴏsᴇ 🇽",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="🖥️️sᴛᴀʀᴛ ʟɪᴠᴇsᴛʀᴇᴀᴍ",
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            )
        ],
        [
            InlineKeyboardButton(
                text="🇽 ᴄʟᴏsᴇ 🇽",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text="🔊ᴘʟᴀʏ ᴀᴜᴅɪᴏ",
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="️📽️ᴘʟᴀʏ ᴠɪᴅᴇᴏ",
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="🇽 ᴄʟᴏsᴇ 🇽",
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons


## Cpanel Markup


def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="𓊕 ᴘᴀᴜsᴇ", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▷ ʀᴇsᴜᴍᴇ",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="sᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="⌧ sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="️◁",
                callback_data=f"Pages Back|0|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="◁ ʙᴀᴄᴋ ▷",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"Pages Forw|0|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons


def panel_markup_2(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔇 ᴍᴜᴛᴇ", callback_data=f"ADMIN Mute|{chat_id}"
            ),
            InlineKeyboardButton(
                text="🔊ᴜɴᴍᴜᴛᴇ",
                callback_data=f"ADMIN Unmute|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⇄ sʜᴜғғʟᴇ",
                callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
            InlineKeyboardButton(
                text=" ∞ ʟᴏᴏᴘ", callback_data=f"ADMIN Loop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"Pages Back|1|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="◁ ʙᴀᴄᴋ ▷",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="️▷",
                callback_data=f"Pages Forw|1|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons


def panel_markup_3(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="|◁ 10 sᴇᴄᴏɴᴅ ",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            InlineKeyboardButton(
                text="▷| 10 sᴇᴄᴏɴᴅ ",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷| 30 sᴇᴄᴏɴᴅ  ",
                callback_data=f"ADMIN 3|{chat_id}",
            ),
            InlineKeyboardButton(
                text="▷| 30 sᴇᴄᴏɴᴅ ",
                callback_data=f"ADMIN 4|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="️◁",
                callback_data=f"Pages Back|2|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="◁ ʙᴀᴄᴋ ▷",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="️▷",
                callback_data=f"Pages Forw|2|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons

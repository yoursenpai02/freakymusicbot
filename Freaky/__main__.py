import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

from Freaky.utilities import config
from Freaky.utilities.config.config import BANNED_USERS
from Freaky import app, bot, LOGGER
from Freaky.modules.core.call import Champu
from Freaky.plugins import ALL_MODULES
from Freaky.modules.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Freaky").error(
            "🥀 𝐍𝐨 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐂𝐥𝐢𝐞𝐧𝐭𝐬 [𝐕𝐚𝐫𝐬] 𝐅𝐨𝐮𝐧𝐝❗"
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫").warning(
            "🥀 𝐍𝐨 𝐒𝐩𝐨𝐭𝐢𝐟𝐲 𝐕𝐚𝐫𝐬 𝐃𝐞𝐟𝐢𝐧𝐞𝐝❗...\n🌷 𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 𝐖𝐨𝐧'𝐭 𝐁𝐞 𝐀𝐛𝐥𝐞 𝐓𝐨 𝐏𝐥𝐚𝐲 𝐒𝐩𝐨𝐭𝐢𝐟𝐲 𝐐𝐮𝐞𝐫𝐢𝐞𝐬❗..."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await bot.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Freaky.plugins" + all_module)
    LOGGER("Freaky.modules.plugins").info(
        "🥀 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐈𝐦𝐩𝐨𝐫𝐭𝐞𝐝 𝐀𝐥𝐥 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 🌿 "
    )
    await app.start()
    await Champu.start()
    try:
        await Champu.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫").error(
            "[𝐄𝐫𝐫𝐨𝐫] - \n\n🥀 𝐏𝐥𝐞𝐚𝐬𝐞 𝐓𝐮𝐫𝐧 𝐎𝐧 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐎𝐟 𝐘𝐨𝐮𝐫 𝐋𝐨𝐠𝐠𝐞𝐫 𝐆𝐫𝐨𝐮𝐩❗..."
        )
        sys.exit()
    except:
        pass
    await Champu.decorators()
    LOGGER("𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫").info("🥳 𝐂𝐨𝐧𝐠𝐫𝐚𝐭𝐮𝐥𝐚𝐭𝐢𝐨𝐧𝐬, 𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 ✨...")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Freaky").info("💐 𝐒𝐲𝐬𝐭𝐞𝐦 𝐒𝐭𝐨𝐩𝐩𝐞𝐝, 𝐆𝐨𝐨𝐝𝐛𝐲𝐞❗...")

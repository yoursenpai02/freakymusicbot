# Champu Halder
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client

from Freaky.utilities import config
from Freaky.console import LOGGER

TEMP_MONGODB = "mongodb+srv://champujis13:shivanshudeo@cluster0.zlafrmn.mongodb.net/?retryWrites=true&w=majority"


if config.MONGO_DB_URL is None:
    LOGGER(__name__).warning(
        "❄️ ɴᴏ ᴍᴏɴɢᴏ ᴅʙ ᴜʀʟ ғᴏᴜɴᴅ ❄️𝐧𝐝 ✨...\n\n ❤️ʏᴏᴜʀ ʙᴏᴛ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ\nᴄʜᴀᴍᴘᴜ ᴅᴀᴛᴀʙᴀsᴇ𝐛𝐚𝐬𝐞 ✨ ..."
    )
    temp_client = Client(
        "Champu",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
    temp_client.start()
    info = temp_client.get_me()
    username = info.username
    temp_client.stop()
    _mongo_async_ = _mongo_client_(TEMP_MONGODB)
    _mongo_sync_ = MongoClient(TEMP_MONGODB)
    mongodb = _mongo_async_[username]
    pymongodb = _mongo_sync_[username]
else:
    _mongo_async_ = _mongo_client_(config.MONGO_DB_URL)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URL)
    mongodb = _mongo_async_.Champu
    pymongodb = _mongo_sync_.Champu

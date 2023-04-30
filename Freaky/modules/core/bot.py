import sys
from pyrogram import Client
from Freaky.utilities import config
from Freaky.console import LOGGER


class Bot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"❄️ sᴛᴀʀᴛɪɴɢ ʏᴏᴜʀ ʙᴏᴛ ✨️...")
        super().__init__(
            "AdityaPlayer",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID,
                f"**━━━━━━━━━━━━━━━━━━━**\n**❄️ʙᴏᴛ sᴛᴀʀᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ✨️**\n**━━━━━━━━━━━━━━━━━━━**\n**❤️ ɴᴀᴍᴇ ›** {self.name}\n**🌸 ʟɪɴᴋ ›** @{self.username}\n**📝 ɪᴅ ›** `{self.id}`\n━━━━━━━━━━━━━━━━━━━\n**🔥 ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ ᴄʜᴧᴍᴘᴜ ](https://t.me/TheShivanshu) **\n**━━━━━━━━━━━━━━━━━━━**",
              disable_web_page_preview=True
            )
        except:
            LOGGER(__name__).error(
                "❄️ ᴘʟᴇᴀsᴇ, ғɪʀsᴛ ᴀᴅᴅ ᴍᴜsɪᴄ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ʟᴏɢ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴀɴ ᴀᴅᴍɪɴ ✨️..."
            )
            sys.exit()
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "❄️ ᴘʟᴇᴀsᴇ ᴘʀᴏᴍᴏᴛᴇ  ʙᴏᴛ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ʟᴏɢ ɢʀᴏᴜᴘ ✨️..."
            )
            sys.exit()
        LOGGER(__name__).info(f"━━━━━━━━━━━━━━━━━━━\n❄️ʙᴏᴛ sᴛᴀʀᴛ sᴜᴄᴄᴇssғᴜʟʟʏ✨️\n━━━━━━━━━━━━━━━━━━━\n❤️ ɴᴀᴍᴇ » {self.name}\n🌸 ʟɪɴᴋ » {self.username}\n📝 ɪᴅ » `{self.id}`\n━━━━━━━━━━━━━━━━━━━\n🔥 ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ ᴄʜᴧᴍᴘᴜ ](https://t.me/TheShivanshu).\n━━━━━━━━━━━━━━━━━━━")
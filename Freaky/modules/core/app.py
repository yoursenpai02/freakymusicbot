import sys
from pyrogram import Client
from Freaky.utilities import config
from Freaky.console import LOGGER

assistants = []
assistantids = []


class App(Client):
    def __init__(self):
        self.one = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"❄️ sᴛᴀʀᴛᴇᴅ ᴀssɪsᴛᴀɴᴛ ᴄʟɪᴇɴᴛs ✨️")
        if config.STRING1:
            await self.one.start()
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            try:
                await self.one.join_chat("TheShivanshu")
                await self.one.join_chat("ll_Champu_ll")
                await self.one.join_chat("Chatting_Club_Indian_Friends")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID,
                    f"**━━━━━━━━━━━━━━━━━━━**\n**❄️ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ✨️**\n**━━━━━━━━━━━━━━━━━━━**\n**❤️ ɴᴀᴍᴇ ›** {self.one.name}\n**🌸 ʟɪɴᴋ ›** @{self.one.username}\n**📝 ɪᴅ ›** `{self.one.id}`\n**━━━━━━━━━━━━━━━━━━━**\n**[ᴄʜᴧᴍᴘᴜ](https://t.me/ll_Champu_ll).**\n**━━━━━━━━━━━━━━━━━━━**",
                  disable_web_page_preview=True
                )
            except:
                LOGGER(__name__).error(
                    f"🎃ᴀssɪsᴛᴀɴᴛ ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss\nʟᴏɢ's ɢʀᴏᴜᴘ✨️ ...\n\n❄️ᴘʟᴇᴀsᴇ ᴀᴅᴅ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴀs\nᴀɴ ᴀᴅᴍɪɴ🎀 ..."💞 ..."
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🎄 ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ 🌿 ᴀs{self.one.name} ✨..."
            )
        if config.STRING2:
            await self.two.start()
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
            try:
                await self.two.join_chat("TheShivanshu")
                await self.two.join_chat("ll_Champu_ll")
                await self.two.join_chat("Chatting_Club_Indian_Friends")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID,
                    f"**━━━━━━━━━━━━━━━━━━━**\n**❄️ᴀssɪsᴛᴀɴᴛ 2 sᴛᴀʀᴛᴇᴅ✨️**\n**━━━━━━━━━━━━━━━━━━━**\n**❤️ ɴᴀᴍᴇ ›** {self.one.name}\n**🌸 ʟɪɴᴋ ›** @{self.one.username}\n**📝 ɪᴅ ›** `{self.one.id}`\n**━━━━━━━━━━━━━━━━━━━**\n**[ᴄʜᴧᴍᴘᴜ](https://t.me/ll_Champu_ll).**\n**━━━━━━━━━━━━━━━━━━━**",
                  disable_web_page_preview=True
                )
            except:
                LOGGER(__name__).error(
                    f"🎃ᴀssɪsᴛᴀɴᴛ 2 ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss\nʟᴏɢ's ɢʀᴏᴜᴘ✨️ ...\n\n❄️ᴘʟᴇᴀsᴇ ᴀᴅᴅ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴀs\nᴀɴ ᴀᴅᴍɪɴ🎀 . 💞 ..."💞 ..."
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🎄 ᴀssɪsᴛᴀɴᴛ 2 sᴛᴀʀᴛᴇᴅ 🌿 ᴀs {self.two.name} ✨..."
            )
        if config.STRING3:
            await self.three.start()
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.three.name = get_me.first_name
            try:
                await self.three.join_chat("TheShivanshu")
                await self.three.join_chat("ll_Champu_ll")
                await self.three.join_chat("Chatting_Club_Indian_Friends")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID,
                    f"**━━━━━━━━━━━━━━━━━━━**\n**❄️ᴀssɪsᴛᴀɴᴛ 3 sᴛᴀʀᴛᴇᴅ✨️**\n**━━━━━━━━━━━━━━━━━━━**\n**❤️ ɴᴀᴍᴇ ›** {self.one.name}\n**🌸 ʟɪɴᴋ ›** @{self.one.username}\n**📝 ɪᴅ ›** `{self.one.id}`\n**━━━━━━━━━━━━━━━━━━━**\n**[ᴄʜᴧᴍᴘᴜ](https://t.me/ll_Champu_ll).**\n**━━━━━━━━━━━━━━━━━━━**",
                  disable_web_page_preview=True
                )
            except:
                LOGGER(__name__).error(
                    f"🎃ᴀssɪsᴛᴀɴᴛ 3 ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss\nʟᴏɢ's ɢʀᴏᴜᴘ✨️ ...\n\n❄️ᴘʟᴇᴀsᴇ ᴀᴅᴅ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴀs\nᴀɴ ᴀᴅᴍɪɴ🎀 . 💞 💞 ..."
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🎄 ᴀssɪsᴛᴀɴᴛ 3 sᴛᴀʀᴛᴇᴅ 🌿 ᴀs {self.three.name} ✨..."
            )
        if config.STRING4:
            await self.four.start()
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.four.name = get_me.first_name
            try:
                await self.four.join_chat("TheShivanshu")
                await self.four.join_chat("ll_Champu_ll")
                await self.four.join_chat("Chatting_Club_Indian_Friends")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID,
                    f"**━━━━━━━━━━━━━━━━━━━**\n**❄️ᴀssɪsᴛᴀɴᴛ  4 sᴛᴀʀᴛᴇᴅ✨️**\n**━━━━━━━━━━━━━━━━━━━**\n**❤️ ɴᴀᴍᴇ ›** {self.one.name}\n**🌸 ʟɪɴᴋ ›** @{self.one.username}\n**📝 ɪᴅ ›** `{self.one.id}`\n**━━━━━━━━━━━━━━━━━━━**\n**[ᴄʜᴧᴍᴘᴜ](https://t.me/ll_Champu_ll).**\n**━━━━━━━━━━━━━━━━━━━**",
                  disable_web_page_preview=True
                )
            except:
                LOGGER(__name__).error(
                    f"🎃ᴀssɪsᴛᴀɴᴛ 4 ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss\nʟᴏɢ's ɢʀᴏᴜᴘ✨️ ...\n\n❄️ᴘʟᴇᴀsᴇ ᴀᴅᴅ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴀs\nᴀɴ ᴀᴅᴍɪɴ🎀 ..."
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🎄 ᴀssɪsᴛᴀɴᴛ 4  sᴛᴀʀᴛᴇᴅ 🌿 ᴀs  {self.four.name} ✨..."
            )
        if config.STRING5:
            await self.five.start()
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.five.name = get_me.first_name
            try:
                await self.five.join_chat("TheShivanshu")
                await self.five.join_chat("ll_Champu_ll")
                await self.five.join_chat("Chatting_Club_Indian_Friends")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID,
                    f"**━━━━━━━━━━━━━━━━━━━**\n**❄️ᴀssɪsᴛᴀɴᴛ 5 sᴛᴀʀᴛᴇᴅ✨️**\n**━━━━━━━━━━━━━━━━━━━**\n**❤️ ɴᴀᴍᴇ ›** {self.one.name}\n**🌸 ʟɪɴᴋ ›** @{self.one.username}\n**📝 ɪᴅ ›** `{self.one.id}`\n**━━━━━━━━━━━━━━━━━━━**\n**[ᴄʜᴧᴍᴘᴜ](https://t.me/ll_Champu_ll).**\n**━━━━━━━━━━━━━━━━━━━**",
                  disable_web_page_preview=True
                )
            except:
                LOGGER(__name__).error(
                    f"🎃ᴀssɪsᴛᴀɴᴛ 5 ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss\nʟᴏɢ's ɢʀᴏᴜᴘ✨️ ...\n\n❄️ᴘʟᴇᴀsᴇ ᴀᴅᴅ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴀs\nᴀɴ ᴀᴅᴍɪɴ🎀"
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🎄 ᴀssɪsᴛᴀɴᴛ 5 sᴛᴀʀᴛᴇᴅ 🌿 ᴀs {self.five.name} ✨..."
            )
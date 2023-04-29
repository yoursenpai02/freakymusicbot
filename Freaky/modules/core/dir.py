# Champu Halder

import os
import sys
from os import listdir, mkdir

from Freaky.console import LOGGER


def dirr():
    if "Freaky" not in listdir():
        LOGGER(__name__).warning(
                    f"❄️ ᴛʜɪs ʀᴇᴘᴏ ɪs ɴᴏᴛ ᴏʀɪɢɪɴᴀʟ\nᴘʟᴇᴀsᴇ ᴜsᴇ ᴏʀɪɢɪɴᴀʟ ʀᴇᴘᴏ✨..."
                )
        sys.exit()
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".jpeg"):
            os.remove(file)
    if "downloads" not in listdir():
        mkdir("downloads")
    if "cache" not in listdir():
        mkdir("cache")
    LOGGER(__name__).info("❄️ ᴀʟʟ ᴅɪʀᴇᴄᴛᴏʀɪᴇs ᴜᴘᴅᴀᴛᴇᴅ ✨...")

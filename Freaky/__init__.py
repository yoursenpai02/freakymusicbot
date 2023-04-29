# Champu PLAYER

from Freaky.modules.core.app import App
from Freaky.modules.core.bot import Bot
from Freaky.modules.core.dir import dirr
from Freaky.modules.core.git import git
from Freaky.misc import dbb, heroku, sudo

from .console import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
bot = Bot()

# Assistant Client
app = App()

from Freaky.utilities.media import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

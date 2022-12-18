import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("API_ID",17568815))
    API_HASH = os.environ.get("API_HASH","177622d39f23e7c3d015f3d6ebaacd31")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5740066159:AAHIkaBc1Nz2K3vbwf8KQy-u0ASUcHQhI0A")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","oldtaggerbot")
    BOT_NAME = os.environ.get("BOT_NAME","OLD TAGGER")
    BOT_ID = int(os.environ.get("BOT_ID",5740066159))
    SUDO_USERS = os.environ.get("SUDO_USERS","AnonyumAz").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT","oldsupport")
    OWNER_ID = int(os.environ.get("OWNER_ID",5508658149))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME","SatisAzOwner")
    IMG_1 = os.environ.get("IMG_1", "https://telegra.ph/file/cce7cc0f861e755ab775e.jpg")

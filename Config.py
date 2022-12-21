import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("API_ID", 10300036))
    API_HASH = os.environ.get("API_HASH", "79c295e05c970ddd724f0762ba275104")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5806469241:AAFpSXKzFOQqk0jjb0nE4hIFmvSbAyh01jY")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TaggerLuciBot")
    BOT_NAME = os.environ.get("BOT_NAME", "TaggerBot")
    BOT_ID = int(os.environ.get("BOT_ID",5806469241))
    SUDO_USERS = os.environ.get("SUDO_USERS", "ordayam_5_deqiqeye").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "oldsupport")
    OWNER_ID = int(os.environ.get("OWNER_ID",2124305832))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "ordayam_5_deqiqeye")
    IMG_1 = os.environ.get("IMG_1", "https://telegra.ph/file/cce7cc0f861e755ab775e.jpg")

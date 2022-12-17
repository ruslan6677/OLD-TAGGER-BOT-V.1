import os


class Config():
    # Bu dəyərləri my.telegram.org saytından əldə edin
    #>>> https://my.telegram.org
    API_ID = int(os.environ.get("API_ID","15954332"))
    API_HASH = os.environ.get("API_HASH","85adea6f1eaf068b707703b4846a9ced")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5681957815:AAFhFXCA5TzZChgvqtk2Ef8QV17ObX-k4ZU")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","oldtaggerbot")
    BOT_NAME = os.environ.get("BOT_NAME","OLD TAGGER")
    BOT_ID = int(os.environ.get("BOT_ID","5740066159-"))
    SUDO_USERS = os.environ.get("SUDO_USERS","AnonyumAz").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT","oldsupport")
    OWNER_ID = int(os.environ.get("OWNER_ID","5508658149"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME","SatisAzOwner")

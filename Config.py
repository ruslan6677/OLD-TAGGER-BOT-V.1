import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("15954332"))
    API_HASH = os.environ.get("85adea6f1eaf068b707703b4846a9ced")
    BOT_TOKEN = os.environ.get("5740066159:AAH6bGkKO34_81_8WkoWTeQn07orOvyDSQw")
    BOT_USERNAME = os.environ.get("oldtaggerbot")
    BOT_NAME = os.environ.get("OLD TAGGER")
    BOT_ID = int(os.environ.get("5740066159"))
    SUDO_USERS = os.environ.get("5354746778").split()
    SUPPORT_CHAT = os.environ.get("oldsupport")
    OWNER_ID = int(os.environ.get("5508658149"))
    OWNER_USERNAME = os.environ.get("SatisAzOwner")

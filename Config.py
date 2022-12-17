import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("API_ID",15954332)) 
    API_HASH = os.environ.get("API_HASH","85adea6f1eaf068b707703b4846a9ced") 
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5740066159:AAH6bGkKO34_81_8WkoWTeQn07orOvyDSQw") 
    BOT_USERNAME = os.environ.get("BOT_USERNAME","oldtaggerbot")
    BOT_NAME = os.environ.get("BOT_NAME","OLD TAGGER") 
    BOT_ID = int(os.environ.get("BOT_ID",5740066159))
    SUDO_USERS = os.environ.get("SUDO_USERS",5134595693).split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT","oldsupport")
    OWNER_ID = int(os.environ.get("OWNER_ID",5508658149))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME","SatisAzOwner")

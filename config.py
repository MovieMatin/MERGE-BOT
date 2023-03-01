import os


class Config(object):
    API_HASH = os.environ.get("409da5b68ad699091fa72b381921f0e5")
    BOT_TOKEN = os.environ.get("6285202665:AAFRmXc-l2wP_04NtlAkfau0_iDZWIZvKBE")
    TELEGRAM_API = os.environ["15236804"]
    OWNER = os.environ.get("1963114305")
    OWNER_USERNAME = os.environ.get("Md_Matin_Ashraf")
    PASSWORD = os.environ.get("QAZ1qaz@QAZ1qaz@")
    DATABASE_URL = os.environ.get("mongodb+srv://MdMatin:x7bdggKJ9zb9JSK@cluster0.89bzvjn.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("-1001812984233")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]

import os


class Config(object):
    API_HASH = "409da5b68ad699091fa72b381921f0e5"
    BOT_TOKEN = "6285202665:AAFRmXc-l2wP_04NtlAkfau0_iDZWIZvKBE"
    TELEGRAM_API = 15236804
    OWNER = "1963114305"
    OWNER_USERNAME = "Md_Matin_Ashraf"
    PASSWORD = "ThanksMatin"
    DATABASE_URL = "mongodb+srv://MdMatin:x7bdggKJ9zb9JSK@cluster0.89bzvjn.mongodb.net/?retryWrites=true&w=majority"
    LOGCHANNEL = "-1001812984233"  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = BQBYOZqJArhcmKFJbRb_iFHnCWx65L2A5gktEXZTAScwQMJ_oWElIaAgU7wsWh5PCc_luUrZZrNHyC3mqZ7rWOgbUZZjxE06ul4hFEk-GEfyuLR98lv6H3o8t37TK525Y9mFDbabKz6a9yCDAqMecw7b15rHUOaJr-acz-A5F_-Fyc2vq2FBP50tXuUGOt17yZ1zzr1loTyugObT7qpZWlSYgGy0GLun_1McWlZy4WjZRTyS6iQCG3kvpC7x2yhRzgYKdzyNeyrVs3aQhHqqyX2eholwzeS1EXgs8tBC0udsrYWQAjlVpn7G31CCuDJSJ1l-Bf_VYTbgXwZvlm04CKe8dQK_QQA
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]

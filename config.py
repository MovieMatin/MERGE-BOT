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
    USER_SESSION_STRING = "BQCHW000U83CBje0jPU8smX9J4E2tU6GCD-yb3tpAxbH8cZigD7UVbZRf-E_K2aOKAya_bgERS0AhhVvyKRzVAutrZebcNSCPtNF-0XKdQDxNUOAnpj8HAk7maiOT9C5_GGN__43uvheaB5TbifkBSS-dYOgWK6AJNIaUgnufh0hBf_FGN5fiIj-iRuDYhkZ_Ly1wfvkfPyFWx7zbphk1NKwg7qr3HamAYk6GaLcaZxmKLxlfLUXcdgBWzW8_dtkgiTSE2TY3bZlId6BSm6C8rwbrvAqNBs1gsL2JidxpgxPGGE2m6Ne7GEBwYvOnefJA4kQBPP3cGMCLL3tt4ErIYnNdQK_QQA"
    IS_PREMIUM = "True"
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]

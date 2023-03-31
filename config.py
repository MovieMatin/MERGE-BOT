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
    USER_SESSION_STRING = "BQDofsQAt2MgIh8bjpwOGKQ_EBzr9eDX1USc6rRrFH-4lNb99v5JMg-XwYQz24fPe9YMIbfgbMVtmkhgiGIhwP1zEaLpU2_GX18XE_nsaAE7Utd3Sl4tfO_MkQodyQ3bQiEPsavenLKAknj8vPrpRB0xQ4TlShY8kqx1TpVHxj-NXuXxVGqkbIHtPa3_HiUK98atd9mgbL_YG1XCas_r8Sz_nPytJYJqF3YCttD-8viOagB1YadW2zTtIs7iF--Hh53Sc7fMbkfw8fWk0P-uGvVLzfWLv3nEhLUF_em49_K_4weY45TsCFXB3mHdzTVxTqn0fkupABwfoNDkRU0cDKx9J0wAMwAAAAB1Ar9BAA"
    IS_PREMIUM = "True"
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]

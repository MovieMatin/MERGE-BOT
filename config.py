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
    USER_SESSION_STRING = "BQDofsQAfFN0lGXa8wHQm8GEiZVjiIv7vM6P0pgKjnH9Lc75NvEGobtXt6mFoWBXBwbj-ErE9_fzDv97LyLFDWM9lMdrWdOemncbED4trDMHzJIS81LHxCagcDRB-vQjFNWbMjn1iqAbE4Myy763w7UH0VvXtLT_POpc94ksMZVt_IMpgpu9s9IWhAMfmdRlbv0xhTbek1n8rZ79tOmeVAPFTSBjS2zanPFtmS93_iipXDzx-OPn2a99ynJZozRJOn7z1vZYqLe4u1W5qtaXzyuqVGeMuak8yBtyeBmXgGjKsZ9Hs3kTIHPGOd97ZeK4kEumfQ01-CpjCaIkgvhWnsCZUaGJOgAAAAB1Ar9BAA"
    IS_PREMIUM = "True"
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]

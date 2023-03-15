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
    USER_SESSION_STRING = "BQDofsQAE33VmMoNVVYKKwMcHKlLUuX3rEtL8IqR0IQeg1gkBh0uSZZ7QdbP5j_kEMIDZRMdQGygdwbcQtmR45P8rUIhUZaZHDxTp0mS72_3TwF_7UCtn0n8Z69VEdwEzwEtyKLP0ABdgUK9D4DPGONkHabcIataSjHwxVNIVCBQpR4fNtRJ3aVsbML9cOIQClSIt1G6mU9F3KFJQhzGm0zFug2CNbqlveMpF1Q4uXoE-PRy1SsToxH06FgSlJ8c0ZOCoCQmiE_OPrT0YCCyokbNGVZ9eT0WfcjabVrRXR-DSRvOmRWwc45VOCqs_nre6YhNqb9xeRPVt1pOkLy-P95IidO1WwAAAAB1Ar9BAA"
    IS_PREMIUM = "True"
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]

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
    USER_SESSION_STRING = "BQDofsQAoXGuXHmbZl5X0HwAKGG-L8fUjwGABHU1OP-nA_j9chKLADukczZFNvy7UG11fCh9FaKAUZvAuC-Ushol3Z6yuOluh9a3WyKrabwrGeOTRsrTrzW_gdhRdg2ZyrVDtwYILUP0ae0fYOkvq5bmtx8H8sb0iYUDLPNTcJT3_p1QHl_mAlckgJUmM9sN1lJdQiGmEwav-izFPquaaPLS_iNKjqGM-dWGQiYg2RR4RbXR6faoSy_KNDzhb2X8VLjvqfnOcnI1QuwlUh_NUUmGok0roALUaysSyjft2cFzV8l3s3VoztBIVc_EKH97KIWcHuXiNPYXQ2x4bRJEQ4VBHvktLQAAAAB1Ar9BAA"
    IS_PREMIUM = "True"
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]

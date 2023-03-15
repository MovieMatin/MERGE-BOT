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
    USER_SESSION_STRING = "BQA1n8pqOo92YxshhlSjhsJ2zx72vbNOBlGPPBGaA5xvmmBi63aew6HC093zNeTmw6BzhDAe1wah4p0lGy_InGrr70JhW9Ru2ySH446JbSP1cQGp-55IqFMq1iUsD1l2YffOF3ofsceTS9_nt764RNVbvPFcBbmHde78YdeCNpYowOzXcVpCyuuLjxQ-UCNAJVOKhGZ1VScG53M6_K9D8LL6F1be00JBwTKUb4kkCEL_CYzgSKPSWk6-e3D9oOfqPI7dWFtWmywjwcaxVhwl-3b1ApNq95st-Next4uZ8hzzhwr3ddqmu5-uuqGfniNnbkD4o1JWgMbUgawyDKRv4umkAAAAAHUCv0EA"
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]

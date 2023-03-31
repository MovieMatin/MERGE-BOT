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
    USER_SESSION_STRING = "BQDofsQAF9IAiY040H864RTKMvhRqjyMdKzmWT-UbLcDRdy1KIiZv_bDZYBd5wawIgSaIUNdaiRvq4sWbCGDXN6YvDBT59GjSzaGaNn0TsdzEqQfWkk68FFcStkn1MKfxt5CiLqmAfpMUQwrcCLi3aK4Fby2wIjSUbgjKu6iaZX2k7glP-2MUXwM0GiSe7XrRLWeoOPknFroSUfE_kNbbZv9mveGgmSeCke7RCYZMb8jpOE06GOetgs3GF6zcq3s-kR_ywgi27gEAHs2FP8DVUe7Ol0cSxPu3lYxy_xjQQ8BpUXNJOEHAJ5omJjpSsYTYEr7h7Esxyr8E7jHBZDHlzlCrdIPSwAAAAB1Ar9BAA"
    IS_PREMIUM = "True"
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]

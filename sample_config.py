from os import environ as env

from dotenv import load_dotenv

load_dotenv("config.env")

"""
READ EVERYTHING CAREFULLY!!!
"""


DEPLOYING_ON_HEROKU = (
    True  # Make this False if you're not deploying On heroku/Docker
)


if not DEPLOYING_ON_HEROKU:
    BOT_TOKEN = ""
    SUDOERS = []
    NSFW_LOG_CHANNEL = 
    SPAM_LOG_CHANNEL = 
    ARQ_API_KEY = ""  # Get it from @ARQRobot
else:
    BOT_TOKEN = env.get("BOT_TOKEN", "5940961389:AAGD32HWrBCAEHF-qfzcXyoG_Wdd6P7fbGA")
    SUDOERS = [int(x) for x in env.get("SUDO_USERS_ID", "1715348447").split()]
    NSFW_LOG_CHANNEL = int(env.get("NSFW_LOG_CHANNEL", "-1001743550303"))
    SPAM_LOG_CHANNEL = int(env.get("SPAM_LOG_CHANNEL", "-1001729142523"))
    ARQ_API_KEY = env.get("ARQ_API_KEY", "UIDMSQ-ERPWVS-HVMLIQ-EOSNZQ-ARQ")

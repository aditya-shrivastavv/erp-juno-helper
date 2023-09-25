from main import Main
from dotenv import load_dotenv
import os

load_dotenv()
base_url = os.getenv("ERP_BASE_URL")
username = os.getenv("ERP_USERNAME")
password = os.getenv("ERP_PASSWORD")

with Main() as bot:
    bot.lauch_web(base_url)
    bot.login(username, password)
    bot.openRootPage()